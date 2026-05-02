from django.shortcuts import render

# Data produk (hardcoded)
produk_list = [
    {
        "id": 1,
        "nama": "Sofa Emerald",
        "deskripsi": "Sofa premium berbahan beludru hijau emerald dengan kaki kayu walnut solid. Desain modern yang timeless untuk ruang tamu Anda.",
        "harga": 12500000,
        "kategori": "FURNITUR",
        "gambar": "https://www.rubeza.com/cdn/shop/products/06156.jpg?v=1627984543"
    },
    {
        "id": 2,
        "nama": "Meja Kopi Marble",
        "deskripsi": "Meja kopi dengan permukaan marmer putih Carrara asli dan rangka besi hitam matte. Elegan dan tahan lama.",
        "harga": 4800000,
        "kategori": "FURNITUR",
        "gambar": "https://down-id.img.susercontent.com/file/id-11134207-7r990-lux9dqd41t5ce1@resize_w450_nl.webp"
    },
    {
        "id": 3,
        "nama": "Lampu Meja Brass",
        "deskripsi": "Lampu meja dengan material kuningan (brass) premium bergaya art deco. Memberikan cahaya hangat yang sempurna.",
        "harga": 1950000,
        "kategori": "PENCAHAYAAN",
        "gambar": "https://cdn.ruparupa.io/fit-in/400x400/filters:format(webp)/filters:quality(90)/ruparupa-com/image/upload/Products/10208538_1.jpg"
    },
    {
        "id": 4,
        "nama": "Vas Keramik Artisan",
        "deskripsi": "Vas keramik buatan tangan pengrajin lokal dengan glasir warna sage green. Setiap produk unik dan satu-satunya.",
        "harga": 680000,
        "kategori": "DEKORASI",
        "gambar": "https://gw.alicdn.com/imgextra/i2/2201206798620/O1CN01mLSOYj2DY0wUcsayI_!!2201206798620.jpg"
    },
    {
        "id": 5,
        "nama": "Set Linen Premium",
        "deskripsi": "Set linen 100% cotton Mesir dengan thread count 800. Tersedia dalam palet warna netral yang elegan.",
        "harga": 2200000,
        "kategori": "TEKSTIL",
        "gambar": "https://venettodesign.com/cdn/shop/files/df73389b-470f-4f7c-aa6e-a70c0ae3a683.jpg?v=1698080439&width=800"
    },
    {
        "id": 6,
        "nama": "Kursi Accent Oak",
        "deskripsi": "Kursi accent dengan rangka kayu oak solid dan dudukan berbahan wool tweed. Kenyamanan bertemu estetika.",
        "harga": 5750000,
        "kategori": "FURNITUR",
        "gambar": "https://mebelisadesign.co.id/image/cache/catalog/products/1008/Ottawa-Chair-Kursi-Aksen-Sofa-Santai-Minimalis-Scandinavian-1000x1000.png"
    },
    {
        "id": 7,
        "nama": "Cermin Dinding Arch",
        "deskripsi": "Cermin berbingkai kayu dengan bentuk arch (melengkung) bergaya Mediterania modern. Tinggi 120cm.",
        "harga": 3100000,
        "kategori": "DEKORASI",
        "gambar": "https://s.alicdn.com/@sc04/kf/H4adf7fc46abf492fac8c3b52caabb580C/Wholesale-Custom-Unbreakable-Big-Vintage-Home-Decor-Brown-Wooden-Large-Full-Length-Long-Wall-Mirror.jpg"
    },
    {
        "id": 8,
        "nama": "Karpet Tenun Handmade",
        "deskripsi": "Karpet tenun handmade dengan motif etnik modern, nyaman dan mempercantik ruangan.",
        "harga": 1200000,
        "kategori": "TEKSTIL",
        "gambar": "https://i.etsystatic.com/23352420/r/il/306f34/4581773163/il_fullxfull.4581773163_pya9.jpg"
    },
    {
        "id": 9,
        "nama": "Rak Dinding Minimalis",
        "deskripsi": "Rak dinding multifungsi dengan desain simpel untuk menyimpan buku dan dekorasi.",
        "harga": 450000,
        "kategori": "FURNITUR",
        "gambar": "https://down-id.img.susercontent.com/file/3544a0a0a1880448da606de3a0e4084a"
    },
]

def home(request):
    # Kirim 3 produk teratas untuk ditampilkan di trending section
    produk_terbaru = produk_list[:3]  # Ambil 3 produk pertama
    return render(request, 'home.html', {'produk': produk_terbaru}) 

def daftar_produk(request):
    return render(request, 'produk.html', {'produk': produk_list})

def detail_produk(request, id):
    produk = next((p for p in produk_list if p['id'] == id), None)
    # Maksimal 3 produk, bisa berdasarkan kategori atau random
    related_products = []
    if produk:
        # Ambil produk dengan kategori yang sama (jika ada)
        same_category = [p for p in produk_list if p['id'] != id and p.get('kategori') == produk.get('kategori')]
        
        if len(same_category) >= 3:
            related_products = same_category[:3]
        else:
            # Jika kurang, ambil produk lain yang berbeda kategori
            other_products = [p for p in produk_list if p['id'] != id and p.get('kategori') != produk.get('kategori')]
            related_products = same_category + other_products
            related_products = related_products[:3]
    
    return render(request, 'detail.html', {
        'produk': produk,
        'related_products': related_products
    })

def kontak(request):
    return render(request, 'kontak.html')