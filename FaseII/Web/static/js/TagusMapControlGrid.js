//#-------------------------------------------------------------------------------
//# Name:        TagusMapControlGrid
//# Purpose:
//#
//# Author:      Pedro Gomes
//#
//# Created:     30/10/2013
//# Copyright:   (c) Pedro Gomes 2013
//# Licence:     <your licence>
//#-------------------------------------------------------------------------------

function TagusMapControlGrid() {

    this.getGrid = function(){
        grid = [];
        square0 = [[-28.49766083296346,-83.4521484375],
                    [-24.206889622398023,-76.904296875],
                    [-17.602139123350838,-82.529296875],
                    [-22.024545601240327,-89.12109375]];
        grid.push(square0);
        
        square1 = [[-15.156973713377667,-94.8779296875],
                    [-10.271681232946728,-88.330078125],
                    [-17.476432197195518,-82.6171875],
                    [-21.943045533438166,-88.9892578125]];
        grid.push(square1);
        
        square2 = [[-24.206889622398023,-76.81640625],
                    [-21.16648385820657,-71.71875],
                    [-13.838079936422462, -76.86035156249999 ],
                    [-17.476432197195518,-82.529296875]];
        grid.push(square2);
 
 
        square3 = [[-10.314919285813147,-88.11035156249999],
                    [-6.751896464843362,-83.0126953125],
                    [-14.3069694978258,-78.0029296875],
                    [-17.35063837604883,-82.5732421875]];
        grid.push(square3);

        square4 = [[-6.795535025719518,-83.0126953125],
                    [-4.609278084409823,-79.541015625],
                    [-12.46876014482322,-74.1796875],
                    [-14.349547837185362,-77.47558593749999]];
        grid.push(square4);
        square5 = [[-21.16648385820657,-71.71875],
                    [-13.88074584202559,-76.7724609375],
                    [-11.5230875068685,-72.7734375],
                    [-19.31114335506463,-68.203125]];
        grid.push(square5);
        square6 = [[-4.565473550710278,-79.5849609375],
                    [-2.3284603685731593,-75.41015624999999],
                    [-10.487811882056695,-70.7958984375],
                    [-12.382928338487396,-74.3994140625]];
        grid.push(square6);
        square7 = [[-19.26966529650232,-68.02734375],
                    [-16.846605106396304,-63.54492187500001],
                    [-9.188870084473393,-68.4228515625],
                    [-11.5230875068685,-72.7294921875]];
        grid.push(square7);
        square8 = [[-2.2406396093827206,-75.41015624999999],
                    [-0.08789059053082422,-71.3671875],
                    [-8.276727101164033,-66.97265625],
                    [-10.314919285813147,-70.7958984375]];
        grid.push(square8);
        square9 = [[-16.846605106396304,-63.54492187500001],
                    [-8.885071663468981,-67.939453125],
                    [-6.664607562172573,-63.720703125],
                    [-14.987239525774244,-59.765625]];
        grid.push(square9);        
        
        square10 = [[-16.846605106396304,-63.54492187500001],
                    [-8.885071663468981,-67.939453125],
                    [-6.664607562172573,-63.720703125],
                    [-14.987239525774244,-59.765625]];
        grid.push(square10);
        
        square11 = [[-0.04394530819134536,-71.3232421875],
                    [1.9771465537125645,-67.32421875],
                    [-6.533645130567532,-63.28125],
                    [-8.18974234438369,-66.884765625]];
        grid.push(square11);
        
        square12 = [[-0.08789059053082422,-71.3671875],
                    [1.9332268264771233,-67.32421875],
                    [-6.402648405963884,-63.369140625],
                    [-8.102738577783168,-66.884765625]];
        grid.push(square12);
        
        square13 = [[-14.987239525774244,-59.853515625],
                    [-12.768946439455956,-55.06347656249999],
                    [-4.609278084409823,-59.2822265625],
                    [-6.577303118123875,-63.58886718749999]];
        grid.push(square13);
        
        square14 = [[-14.987239525774244,-59.853515625],
                    [-12.768946439455956,-55.06347656249999],
                    [-4.609278084409823,-59.2822265625],
                    [-6.577303118123875,-63.58886718749999]];
        grid.push(square14);
        
        square15 = [[2.0210651187669897,-67.2802734375],
                    [3.8204080831949407,-63.4130859375],
                    [-4.477856485570586,-59.3701171875],
                    [-6.271618064314864,-63.4130859375]];
        grid.push(square15);
        
        square16 = [[-12.726084296948184,-55.06347656249999],
                    [-11.178401873711785,-51.2841796875],
                    [-2.7674779510920717,-54.9755859375],
                    [-4.521666342614791,-59.0625]];
        grid.push(square16);
        
        square17 = [[3.8204080831949407,-63.369140625],
        [5.61598581915534,-59.10644531249999],
        [-2.7674779510920717,-55.283203125],
        [-4.390228926463384,-59.3701171875]];
        grid.push(square17);
        
        square18 = [[-11.264612212504428,-51.328125],
                    [-9.535748998133627,-47.02148437499999],
                    [-1.0106897682409002,-50.40527343749999],
                    [-2.723583083348398,-54.88769531249999]];
        grid.push(square18);

        square19 = [[5.659718554577286,-59.10644531249999],
            [7.449624260197816,-54.404296875],
            [-1.1425024037061522,-50.88867187499999],
            [-2.811371193331128,-55.283203125]];
        grid.push(square19);

        square20 = [[-9.535748998133627,-46.9775390625],
                    [-8.146242825034385,-42.802734375],
                    [0.615222552406841,-45.791015625],
                    [-0.8349313860427057,-50.185546875]];
        grid.push(square20);
        
        square21 = [[7.449624260197816,-54.404296875],
                    [9.188870084473406,-49.482421875],
                    [0.615222552406841,-46.05468749999999],
                    [-1.0106897682409002,-50.8447265625]];
        grid.push(square21);
        
        square22 = [[-8.102738577783168,-42.84667968749999],
                    [-6.577303118123875,-38.14453125],
                    [2.064982495867104,-41.1328125],
                    [0.6591651462894632,-45.703125]];
        grid.push(square22);
        
        square23 = [[9.232248799418674,-49.43847656249999],
                    [10.833305983642491,-44.4287109375],
                    [2.0210651187669897,-41.5283203125],
                    [0.6591651462894632,-45.87890625]];
        grid.push(square23);
        
        square24 = [[-6.533645130567532,-38.18847656249999],
                    [-5.397273407690891,-33.662109375],
                    [3.513421045640057,-36.3427734375],
                    [2.152813583128846,-41.044921875]];
        grid.push(square24);
        
        square25 = [[10.876464994816295,-44.384765625],
                    [12.082295837363578,-40.25390625],
                    [3.2063329870791444,-37.6611328125],
                    [2.152813583128846,-41.5283203125]];
        grid.push(square25);
        
        square26 = [[-5.44102230371796,-33.8818359375],
                    [-4.302591077119676,-28.7841796875],
                    [4.784468966579375,-30.849609375],
                    [3.5572827265412794,-36.25488281249999]];
        grid.push(square26);
        
        square27 = [[12.082295837363578,-40.25390625],
                    [13.068776734357694,-35.947265625],
                    [4.1711154548674365,-33.7939453125],
                    [3.118576216781991,-37.6611328125]];
        grid.push(square27);
        
        square28 = [[-4.34641127533318,-28.7841796875],
                    [-3.469557303061473,-25.048828125],
                    [5.703447982149503,-26.894531249999996],
                    [4.8282597468669755,-30.761718749999996]];
        grid.push(square28);
        
        square29 = [[13.111580118251661,-35.947265625],
                    [14.093957177836236,-31.596679687499996],
                    [5.090944175033399,-29.70703125],
                    [4.214943141390651,-33.7060546875]];
        grid.push(square29);
        
        square30 = [[-3.381823735328289,-24.960937499999996],
                    [-2.723583083348398,-21.3134765625],
                    [6.402648405963896,-22.8955078125],
                    [5.659718554577286,-26.8505859375]];
        grid.push(square30);
        
        square31 = [[14.136575651477944,-31.552734374999996],
                    [14.859850400601037,-27.861328125],
                    [5.922044619883305,-26.015625],
                    [5.222246513227389,-29.663085937499996]];
        grid.push(square31);
        
        square32 = [[-2.67968661580376,-21.4013671875],
                    [-1.9771465537125645,-15.99609375],
                    [7.144498849647335,-17.402343749999996],
                    [6.402648405963896,-22.8515625]];
        grid.push(square32);
        
        square33 = [[14.902321826141808,-27.773437499999996],
                    [15.496032414238634,-23.73046875],
                    [6.446317749457659,-21.97265625],
                    [5.834616165610072,-25.9716796875]];
        grid.push(square33);
        
        square34 = [[15.580710739162123,-23.73046875],
                    [16.29905101458183,-18.45703125],
                    [7.27529233637217,-17.2265625],
                    [6.533645130567532,-22.060546874999996]];
        grid.push(square34);
        
        return grid;
        }
        

}
        
        
        
        