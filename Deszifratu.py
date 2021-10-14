from collections import Counter

def sarrera(ema):
    h1=input("Aldatu nahi duzun karakterea sartu.")
    h2=input("Bere ordez jarriko den karakterea sartu.")
    return ema.replace(h1, h2)

def deszifratu():
    mezua = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.      AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
    print ("Mezua :", mezua) #Mezua pantailaratu
    karaktereak = Counter(mezua) #Karaktere bakoitza zenbat aldiz agertzen den kontatu
    print(karaktereak) #Goian egindakoa pantailaratu
    print('Gure testuan gehien errepikatzen diren hiru karaktereak hauek dira:') #Counterrek hitzen arteko hutsuneak kontatzen dituenez eta hauek gehien ageri direnak direnez, gehien ageri diren bi karaktereak hartu beharrean hiru hartuko dira
    komunenak=karaktereak.most_common(3) #Gehien ageri diren hiru karaktereak hartu
    print(komunenak)
    print("\n")
    print("Gaztelaniaz 'e' eta 'a' dira gehien erabiltzen diren hizkiak, beraz, textuan gehien ageri diren bi karaktereak hauekin aldatuko dira")
    mezua= mezua.replace(komunenak[1][0], 'e') #Textuan gehien erabiltzen den hizkia 'e'-z aldatu
    mezua= mezua.replace(komunenak[2][0], 'a') #Textuko bigarren hizkirik erabiliena 'a'-z aldatu
    print(mezua)

    mezua= sarrera(mezua)
    aldaketa = "b"
    while aldaketa=="b":
        print(mezua)
        aldaketa=input("Aldaketa gehiago egin nahi dituzu? (b/e) ")
        if aldaketa != "b":
            print("Programa bukatu da.")
            break
        mezua = sarrera(mezua)

deszifratu()