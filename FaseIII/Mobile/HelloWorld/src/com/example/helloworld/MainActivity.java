package com.example.helloworld;

import java.io.IOException;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.ByteArrayEntity;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicHeader;
import org.apache.http.params.BasicHttpParams;
import org.apache.http.params.HttpConnectionParams;
import org.apache.http.params.HttpParams;
import org.apache.http.protocol.HTTP;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.json.JSONStringer;



import android.net.Uri;
import android.net.wifi.WifiManager;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.annotation.SuppressLint;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.IntentFilter;
import android.graphics.Color;
import android.text.method.ScrollingMovementMethod;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.net.wifi.ScanResult;
import android.graphics.PorterDuff;
import android.graphics.drawable.Drawable;
import android.graphics.drawable.Drawable.ConstantState;

public class MainActivity extends Activity {
	private static final String TAG = "HelloWorld";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        launchURL = (Button) findViewById(R.id.button2);
        launchURL.getBackground().setColorFilter(Color.GRAY, PorterDuff.Mode.MULTIPLY);
        editTextUserID = (EditText) findViewById(R.id.editText1);
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }
    
    public boolean toggle = false;
    public CountDownTimer networkScanner ;
    public Button startStopButton ;
    public TextView editText ;
    public Button launchURL;
    public EditText editTextUserID;
    public Drawable tempColorEditText;
    
    /** Called when the user clicks the Send button */
    public void launchURL(View view) {
    	String url = "http://indoorpositionr.qubit.pt";
    	Intent i = new Intent(Intent.ACTION_VIEW);
    	i.setData(Uri.parse(url));
    	startActivity(i);
    }
    
    /** Called when the user clicks the Send button */
    @SuppressLint("NewApi")
	public void sendMessage(View view) {
    	editText = (TextView) findViewById(R.id.textView1);
    	editText.setMovementMethod(new ScrollingMovementMethod());
    	
    	startStopButton = (Button) findViewById(R.id.button1);
    	
    	if(editTextUserID.getText().toString().matches("")){
    		new AlertDialog.Builder(this)
    	    .setTitle("No ID Provided")
    	    .setMessage("Please provide an ID")
    	    .setPositiveButton(android.R.string.ok, new DialogInterface.OnClickListener() {
    	        public void onClick(DialogInterface dialog, int which) { 
    	            // continue with delete
    	        }
    	     })
    	
    	     .show();
    		return;
    	}
    	
    	
    	if(!toggle){
    		/*If not active */
    		editTextUserID.setClickable(false);
    		editTextUserID.setFocusable(false);
    		editTextUserID.setFocusableInTouchMode(false);
    		Log.d(TAG,"EDIT TEXT BK COLOR :");
    		tempColorEditText =editTextUserID.getBackground().getConstantState().newDrawable();
    		editTextUserID.setBackgroundColor(Color.GRAY);
    		
    		startStopButton.setText("Stop");
    		launchURL.getBackground().setColorFilter(null);
    		launchURL.setClickable(true);
    		toggle = true;
    		
    		//HIDE KEYBOARD
    		InputMethodManager mgr = (InputMethodManager) getSystemService(Context.INPUT_METHOD_SERVICE);
    	    mgr.hideSoftInputFromWindow(editText.getWindowToken(), 0);
    	//TextView editText = (TextView) findViewById(R.id.textView1);
    	//editText.setText(Integer.toString(counter));
    	networkScanner = new CountDownTimer(300000, 1000) {

    	     public void onTick(long millisUntilFinished) {
    	    	 
    	    	 editText.setText("seconds remaining: " + millisUntilFinished / 1000);
    	    	 scanWifi(editText,editTextUserID.getText().toString());
    	     }

    	     public void onFinish() {
    	    	 
    	    	 editText.setText("done!");
    	     }
    	  }.start();
    	
    	}else{
    	 /*Else its active then stop it */
    		editTextUserID.setClickable(true);
    		editTextUserID.setFocusable(true);
    		editTextUserID.setFocusableInTouchMode(true);
    		editTextUserID.setBackground(tempColorEditText);
    		startStopButton.setText("Start");
    		networkScanner.cancel();
    		toggle = false;
    		launchURL.setClickable(false);
    		launchURL.getBackground().setColorFilter(Color.GRAY, PorterDuff.Mode.MULTIPLY);
    	}
    }
    
    public void scanWifi(TextView ediTextView, String UserID){
        WifiManager mainWifi;

        mainWifi = (WifiManager) getSystemService(Context.WIFI_SERVICE);

        mainWifi.startScan();
        List<ScanResult> wifiList;
        StringBuilder sb = new StringBuilder();
        commJSON communicationJSON = new commJSON();
        
        wifiList = mainWifi.getScanResults();
        for(int i = 0; i < wifiList.size(); i++){
            sb.append(new Integer(i+1).toString() + ".");
            sb.append((wifiList.get(i).BSSID).toString() +"  "+(wifiList.get(i).SSID).toString()+"  :"+String.valueOf(wifiList.get(i).level));
            
            communicationJSON.addNetwork(wifiList.get(i).BSSID,wifiList.get(i).level);
            sb.append("\n");
        }
        ediTextView.setText(sb);
        
        //Log.d(TAG,"Start WIFI Log :");
        //Log.d(TAG, communicationJSON.networkList.toString());
        //Log.d(TAG,"End WIFI Log :");
        communicationJSON.networkList("mobileID",UserID);
        sendWeb(communicationJSON.get_networkList());
    }
    
    public static class commJSON{
    	JSONObject networkList = new JSONObject();

    	public JSONObject get_networkList() {
			JSONObject tmpReturn = new JSONObject();
			try {
				
				tmpReturn.put("mobileData", networkList);
			} catch (JSONException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			return tmpReturn;
		}
    	
    	 
    	public void networkList(String string, String userID) {
    		try {
	    		networkList.put(string, userID);
	    		
			} catch (JSONException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		}


		public  void addNetwork(String BSSID, int level){
    		
    		try {
	    		networkList.put(BSSID, level);
	    		
			} catch (JSONException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    		
    		
    	}
    	
    }
    
    private class SendWebData extends AsyncTask<String, Integer, Void> {
    	@Override
		protected Void doInBackground(String... params) {
        	try {
      		  String url = "http://indoorpositionr.qubit.pt/_add_mobile_location_data";   

      		  HttpClient httpclient = new DefaultHttpClient();
      		  HttpPost httppost = new HttpPost(url);
      		  httppost.setHeader("Accept", "application/json");
      		  httppost.setHeader("Content-type", "application/json");
      		  StringEntity se = new StringEntity(json.toString(), "UTF-8");
      		  se.setContentType("text/json;charset=UTF-8");
      		  
      		  Log.d(TAG,"Start Network Log :");
	      	  Log.d(TAG,se.getContent().toString());
	      	  Log.d(TAG,"End Network Log :");
      		  httppost.setEntity(se);

      		  // Execute HTTP Post Request
      		  HttpResponse response = httpclient.execute(httppost);
      		  
      		  
      		} catch (ClientProtocolException e) {
      			// TODO Auto-generated catch block
      			e.printStackTrace();
      		} catch (IOException e) {
      			// TODO Auto-generated catch block
      			e.printStackTrace();
      		}
        	
        	this.cancel(true);
			return null;
        }
    	JSONObject json;
    	
    	public SendWebData(JSONObject jsonRecieved) {
			this.json = jsonRecieved;
		}




      	  
    }
    
   public boolean sendWeb(JSONObject json){
	   new SendWebData(json).execute();
	   return true;
   }


    
}
