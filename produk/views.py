from django.shortcuts import render

# Data produk (hardcoded)
produk_list = [
    {
        "id": 1,
        "nama": "Laptop",
        "deskripsi": "Laptop untuk kerja",
        "harga": 10000000,
        "gambar": "https://png.pngtree.com/background/20230526/original/pngtree-rainbow-block-laptop-close-up-picture-image_2744631.jpg"
    },
    {
        "id": 2,
        "nama": "HP",
        "deskripsi": "Smartphone canggih",
        "harga": 5000000,
        "gambar": "https://images.macrumors.com/t/pxdcoJyi0XOct0uaY0E8tZkHBy4=/2500x/article-new/2025/07/iPhone-17-Pro-on-Desk-Centered-1.jpg"
    },
    {
        "id": 3,
        "nama": "Headset",
        "deskripsi": "Headset gaming",
        "harga": 750000,
        "gambar": "https://gamingsnap.com/wp-content/uploads/2020/09/DF3ToOsXgAA953t-1024x695.jpg"
    },
]

def home(request):
    return render(request, 'home.html')

def daftar_produk(request):
    return render(request, 'produk.html', {'produk': produk_list})

def detail_produk(request, id):
    produk = next((p for p in produk_list if p['id'] == id), None)
    return render(request, 'detail.html', {'produk': produk})

def kontak(request):
    return render(request, 'kontak.html')