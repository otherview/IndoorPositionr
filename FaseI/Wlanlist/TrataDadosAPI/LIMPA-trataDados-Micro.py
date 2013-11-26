


if __name__ == '__main__':

        with open("listings_dbm_Micro.csv") as infile:
                for line in infile:
                        linha = line.strip().split(",")
                        linha.pop()
                        doispontos = False
                        print linha[0]+",",
                        print linha[1]+",",
                        for valor in linha:
                            if doispontos and ":" not in valor :
                                    print valor+",",
                            if ":" in valor:
                                    doispontos = False
                            if "1E:0" in valor:
                                    doispontos = True
                                    print valor+",",
                        print " "
                                
                    