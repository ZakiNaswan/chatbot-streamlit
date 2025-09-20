# Travel Assistant AI Chatbot ✈️🌍

## Ikhtisar Proyek

Ini adalah proyek chatbot AI yang dikembangkan sebagai tugas akhir untuk program **"LLM-Based Tools and Gemini API Integration for Data Scientists"** dari Hacktiv8. Proyek ini bertujuan untuk menciptakan asisten perjalanan virtual yang interaktif dan cerdas, membantu pengguna merencanakan liburan mereka dengan memberikan informasi dan saran berbasis AI.

Aplikasi ini dibangun menggunakan **Streamlit**, sebuah *framework* Python yang memungkinkan pembuatan aplikasi web interaktif dengan cepat, serta memanfaatkan **Google Gemini 1.5 Flash**, sebuah model bahasa besar (LLM) yang kuat, untuk memproses dan merespons pertanyaan pengguna secara alami.

## Fitur Unggulan

-   **Rekomendasi Destinasi**: Memberikan informasi mendalam tentang destinasi populer, termasuk cuaca dan gambaran umum tempat.
-   **Saran Rencana Perjalanan**: Mampu menyarankan tiga aktivitas populer di setiap destinasi untuk membantu pengguna menyusun *itinerary* dasar.
-   **Antarmuka Pengguna Interaktif**: Didesain dengan Streamlit untuk memberikan pengalaman chat yang mulus dan intuitif, lengkap dengan riwayat percakapan.
-   **Otentikasi Aman**: Meminta pengguna untuk memasukkan kunci API secara aman di *sidebar*, tanpa menyimpan kunci tersebut di dalam kode atau repositori.
-   **Tombol Reset**: Fitur untuk memulai ulang percakapan dari awal dengan mudah.

## Cara Menggunakan

### Prasyarat

Sebelum memulai, pastikan Anda telah menginstal:
* **Python 3.8+**
* **Git**

### Instalasi dan Konfigurasi

1.  **Kloning Repositori**:
    Buka terminal dan kloning repositori ini ke komputer Anda.
    ```bash
    git clone [https://github.com/NAMAKU/travel-assistant-chatbot.git](https://github.com/NAMAKU/travel-assistant-chatbot.git)
    cd travel-assistant-chatbot
    ```

2.  **Instal Dependensi**:
    Pasang semua pustaka Python yang diperlukan dari file `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Dapatkan Google AI API Key**:
    Aplikasi ini memerlukan kunci API untuk mengakses model Gemini.
    -   Buka [Google AI Studio](https://aistudio.google.com/app/apikey).
    -   Buat atau salin kunci API Anda.

4.  **Jalankan Aplikasi**:
    Jalankan aplikasi Streamlit dari terminal:
    ```bash
    streamlit run streamlit_chat_app.py
    ```
    Aplikasi akan terbuka otomatis di *browser* Anda. Masukkan kunci API Anda di kolom `Google AI API Key` yang terletak di *sidebar* untuk memulai percakapan.

## Tampilan Aplikasi

Berikut adalah contoh tampilan aplikasi yang sudah berjalan.

![Screenshot Aplikasi Chatbot](https://www.contohgambar.com/chatbot-screenshot.png)

## Tentang Proyek

[cite_start]Proyek ini dikerjakan sebagai bagian dari program **Hacktiv8** dan didukung oleh **AI Opportunity Fund: Asia Pacific**, sebuah inisiatif kolaborasi dengan **AVPN** dan didukung oleh **Google.org** serta **Asian Development Bank**[cite: 4].