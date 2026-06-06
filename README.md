# Project-ASA
**Disusun oleh:**
- **Nama:** Hadrian Shandhy Yudha
- **NIM:** 24060124140207

Selection of the Void Suit in Suichan Mahjong From Game: Neverness to Everness

# Analisis Perbandingan Algoritma Greedy, Dynamic Programming, dan Monte Carlo Tree Search dalam Penentuan Void Suit Sichuan Mahjong pada Game Neverness to Everness

Repositori ini berisi implementasi dari sistem penelitian di atas, yang terbagi ke dalam dua varian kondisi *hand* awal Sichuan Mahjong:

- **[Sichuan_Mahjong_13Tiles](./Sichuan_Mahjong_13Tiles/)**: Implementasi program solver untuk pemain non-dealer dengan 13 *tiles*.
- **[Sichuan_Mahjong_14Tiles](./Sichuan_Mahjong_14Tiles/)**: Implementasi program solver untuk pemain dealer dengan 14 *tiles*.

---

## Abstract

Sichuan Mahjong merupakan salah satu varian permainan mahjong yang mengharuskan pemain menentukan *Void Suit* (*Forbidden Suit* atau Ding Que) sebelum permainan dimulai. Pemilihan *Void Suit* yang tepat menjadi keputusan penting karena dapat memengaruhi peluang pembentukan kombinasi tile selama permainan berlangsung. Penelitian ini bertujuan untuk menganalisis dan membandingkan kinerja algoritma Uniform Cost Search (UCS), Greedy Best First Search (GBFS), A* Search, Dynamic Programming (DP), dan Monte Carlo Tree Search (MCTS) dalam menentukan *Void Suit* berdasarkan kondisi hand awal pemain. Sistem yang dikembangkan menggunakan metode Template Matching untuk mengenali tile dari tangkapan layar permainan Sichuan Mahjong pada Neverness to Everness. Hasil identifikasi tile kemudian direpresentasikan berdasarkan frekuensi suit Character, Bamboo, dan Dot sebagai masukan bagi setiap algoritma. Pengujian dilakukan menggunakan beberapa sampel hand awal pada kondisi dealer dan non-dealer. Hasil penelitian menunjukkan bahwa seluruh algoritma mampu memberikan rekomendasi *Void Suit* sesuai dengan komposisi tile yang dimiliki pemain. Sistem yang diusulkan berhasil mengintegrasikan pengolahan citra dan algoritma pencarian sebagai pendukung pengambilan keputusan dalam penentuan *Void Suit* pada permainan Sichuan Mahjong.

**Keywords**— Sichuan Mahjong, Void Suit, Template Matching, Uniform Cost Search, Greedy Best First Search, A* Search, Dynamic Programming, Monte Carlo Tree Search.
