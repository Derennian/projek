Projek yang telah saya buat berupa discord bot yang dapat melakukan beberapa command unik. Bot yang sudah saya buat dapat melakukan beberapa hal seperti tnaggapan atas apa yang kita chat/tulis, menunjukkan waktu dini, dan juga dapat melakukan roll dari sebuah dadu 1-12 (berupa acak).

cara menggunakan bot tersebut sangatlah mudah, kita hanya perlu mengetik kata-kata yang ingin kita tulis, seperti Hello, roll 6, roll 12, lagu mars igs, dan lain-lain.

ada juga command khusus seperti "!timestamp", yaitu untuk menunjukkan waktu di tempat kita berada, "!google netflix", untuk membuka link menuju beranda netflix, "!google youtube", untuk membuka link youtube, dan juga "!google spotify" untuk membuka spotify dari website.
 
 
Tutorial = 
untuk permulaan, kita harus membuat main dari sebuah coding terlebih dahulu. maka dari itu, saya membuat main.py yang berisikan import bot (agar dapat melaksanakan program bot kita dari bot.py yang sudah kita buat), lalu kita menuliskan if __name__ == '__main__':
    bot.run_discord_bot() agar bot tersebut dapat dihidupkan di dalam discord.

    bot.py = pada bagian bot.py, saya memasukkan beberapa command seperti import discord (untuk dapat dialihkan ke app discord, dan juga RESPONSES, agar hasil dari rsesponses.py yang telah dibuat dapat disalurkan ke bot.py). lalu, saya memmbuat def send_message yang bertujuan agar bot tersebut dapat merespon dengan apa yang kita hendak bicarakan kepada bot tesebut. selanjutnya, saya memasukkan instance dan juga bot TOKEN saya agar bot saya dapat dihidupkan dan dapat melakukan command" yang telah saya buat. lalu, pada bagian def on_ready, saya membaut code tersebut agar saaat pycharm dimulai, akan ada tulisan notifikasi jika bot saya telah dihupkan dan dapat dijalkan command"nya dengan baik pada app discord. dan terakhir, pada command def user_message, saya memvuat hal tersebut agar pada pycharm dapat diketahui apa saja command yang dichat oleh user" dalam discord tersebut, dan apa saja yang akan ditulis oleh bot yang telah saya buat.

    responses.py = pada file ini, saya menggunakan if untuk melakukan beberapa command" yang berbeda. contohnya seperti  if p_message == 'hello':
        return 'hey there mang', yang artinya bot akan membalas "hey the mang" saat user menulis kata "hello". maish banyak variasi yang saya buat, contohnya seperti "!timestamp" yang berfungsi untuk mengetahui jam berapa di tempat kita berada, dengan menggunakan DATETIME. lalu, saya juga memakai RANDOM agar dapat mengacak 2 dadu yang berbeda, yaitu dadu 6, dan dadu 12. saat diajalankan seperti ini = "roll 12", maka bot akan merespons dengan angka secara acak berdasarkan angka dari 1 sampai 12.


      untuk menyalakan bot tersebut, saya akan menuju ke main.py, lalu menekan tomnol yang berbentuk segitiga ke samping (berwarna hijau). setelah itu, kita menekan tulisan "run 'Main'". jika ada tulisan seperti "bot is now running!(yang telah saya buat pada bot.py)", makan bot tersebut telah dapat digunakan pada server yang telah dimasukkan (pastikan bot tersebut online. jika tidak, mungkin ada masalah error yang terjadi / tidak adanya koneksi pada lingkungan tersebut). Demikian tutorial dan cara pembuatan tentang bagaimana cara membuat discord tersebut, terimakasih Sir.

    
