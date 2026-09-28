"""Modul contoh untuk demonstrasi perbaikan kode sesuai PEP 8."""


def hitung_total(nilai_a, nilai_b, daftar, tambahan):
    """Menghitung total dari beberapa nilai.

    Args:
        nilai_a: Bilangan pertama.
        nilai_b: Bilangan kedua.
        daftar: List berisi bilangan.
        tambahan: Bilangan tambahan.

    Returns:
        Hasil penjumlahan seluruh nilai, atau None jika daftar kosong.
    """
    if not daftar:
        return None
    return nilai_a + nilai_b + daftar[0] + tambahan


def main():
    """Fungsi utama program."""
    print(hitung_total(1, 2, [3], 4))


if __name__ == "__main__":
    main()
