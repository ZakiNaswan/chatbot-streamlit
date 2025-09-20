import streamlit as st  # Untuk membuat antarmuka aplikasi web
from google import genai  # Untuk berinteraksi dengan Google Gemini API

# --- 1. Page Configuration and Title ---

# Setel judul dan keterangan untuk halaman web
st.title("💬 Chatbot Travel Assistant")
st.caption("Chatbot yang akan membantu perencanaan perjalanan menggunakan model Gemini 1.5 Flash")

# --- 2. Sidebar untuk Pengaturan ---

# Buat bagian sidebar untuk pengaturan aplikasi
with st.sidebar:
    # Tambahkan subheader
    st.subheader("Settings")
    
    # Buat input teks untuk Google AI API Key.
    # 'type="password"' menyembunyikan kunci saat diketik.
    google_api_key = st.text_input("Google AI API Key", type="password")
    
    # Buat tombol untuk mereset percakapan.
    # 'help' menyediakan tooltip yang muncul saat kursor diarahkan ke tombol.
    reset_button = st.button("Reset Conversation", help="Clear all messages and start fresh")

# --- 3. Inisialisasi Kunci API dan Klien ---

# Periksa apakah pengguna telah menyediakan kunci API.
if not google_api_key:
    st.info("Please add your Google AI API key in the sidebar to start chatting.", icon="🗝️")
    st.stop()

# Blok kode ini menangani pembuatan klien Gemini API.
# Ia hanya membuat klien baru jika tidak ada atau jika kunci API telah berubah.
if ("genai_client" not in st.session_state) or (getattr(st.session_state, "_last_key", None) != google_api_key):
    try:
        # Jika kondisi terpenuhi, buat klien baru.
        st.session_state.genai_client = genai.Client(api_key=google_api_key)
        # Simpan kunci baru di session state untuk perbandingan nanti.
        st.session_state._last_key = google_api_key
        # Karena kunci berubah, hapus riwayat obrolan yang lama.
        st.session_state.pop("chat", None)
        st.session_state.pop("messages", None)
    except Exception as e:
        # Jika kunci tidak valid, tampilkan pesan error dan hentikan aplikasi.
        st.error(f"Invalid API Key: {e}")
        st.stop()

# --- 4. Manajemen Riwayat Obrolan ---

# Inisialisasi sesi obrolan jika belum ada.
if "chat" not in st.session_state:
    # Buat instance obrolan baru menggunakan model 'gemini-1.5-flash-latest'.
    st.session_state.chat = st.session_state.genai_client.chats.create(model="gemini-1.5-flash-latest")

# Inisialisasi riwayat pesan jika belum ada.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tangani klik tombol reset.
if reset_button:
    # Jika tombol reset diklik, hapus objek obrolan dan riwayat pesan dari memori.
    st.session_state.pop("chat", None)
    st.session_state.pop("messages", None)
    # st.rerun() memberi tahu Streamlit untuk me-refresh halaman dari awal.
    st.rerun()

# --- 5. Tampilkan Pesan Sebelumnya ---

# Loop melalui setiap pesan yang tersimpan di session state.
for msg in st.session_state.messages:
    # Untuk setiap pesan, buat gelembung pesan obrolan dengan peran yang sesuai ("user" atau "assistant").
    with st.chat_message(msg["role"]):
        # Tampilkan konten pesan menggunakan Markdown.
        st.markdown(msg["content"])

# --- 6. Tangani Input Pengguna dan Komunikasi API ---

# Buat kotak input obrolan di bagian bawah halaman.
prompt = st.chat_input("Tanyakan tentang destinasi atau rencana perjalanan...")

# Periksa apakah pengguna telah memasukkan pesan.
if prompt:
    # 1. Tambahkan pesan pengguna ke daftar riwayat pesan.
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 2. Segera tampilkan pesan pengguna di layar.
    with st.chat_message("user"):
        st.markdown(prompt)

    # 3. Dapatkan respons dari asisten.
    try:
        # Gunakan prompt engineering untuk memberikan instruksi spesifik pada model.
        full_prompt = f"""Kamu adalah "Chatbot Travel Assistant". Tugasmu adalah membantu pengguna merencanakan perjalanan mereka.
        Berikan informasi seputar destinasi, tempat wisata, atau tips perjalanan.
        Jika pengguna bertanya tentang destinasi, berikan ringkasan singkat tentang tempat tersebut, cuaca saat ini, dan 3 rekomendasi aktivitas populer.
        Gunakan gaya bahasa yang santai dan informatif.
        Contoh input: "Aku mau liburan ke Bali, ada saran?"
        Contoh output: "Wah, pilihan yang bagus! Bali punya banyak tempat keren. Cuaca di Bali saat ini cerah dan hangat.
        Kamu bisa coba:
        1. Menjelajahi sawah Tegalalang di Ubud.
        2. Bersantai di pantai Kuta atau Seminyak.
        3. Mengunjungi Pura Uluwatu saat matahari terbenam."

        Berikut adalah permintaan dari pengguna:
        {prompt}
        """
        # Kirim prompt yang telah disesuaikan ke Gemini API.
        response = st.session_state.chat.send_message(full_prompt)
        
        if hasattr(response, "text"):
            answer = response.text
        else:
            answer = str(response)

    except Exception as e:
        answer = f"An error occurred: {e}"

    # 4. Tampilkan respons dari asisten.
    with st.chat_message("assistant"):
        st.markdown(answer)
    # 5. Tambahkan respons asisten ke daftar riwayat pesan.
    st.session_state.messages.append({"role": "assistant", "content": answer})