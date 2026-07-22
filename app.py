from flask import Flask, render_template_string

app = Flask(__name__)

# كود المتجر النهائي لي صاوبوه البوتات
STORE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PulseBoost Elite | Social Growth</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    
    <style>
        body { font-family: 'Inter', sans-serif; }
        h1, h2, h3 { font-family: 'Playfair Display', serif; }
        .glass {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100">

    <!-- Navigation Bar -->
    <nav class="sticky top-0 z-50 glass border-b border-slate-800">
        <div class="container mx-auto px-6 py-4 flex justify-between items-center">
            <h1 class="text-2xl font-bold text-orange-500">PulseBoost<span class="text-white">Elite</span></h1>
            <div class="hidden md:flex space-x-8 font-medium">
                <a href="#" class="hover:text-orange-500 transition">Services</a>
                <a href="#" class="hover:text-orange-500 transition">Pricing</a>
                <a href="#" class="hover:text-orange-500 transition">FAQ</a>
            </div>
            <button id="cart-btn" class="relative p-2 bg-orange-600 rounded-full hover:bg-orange-500 transition">
                🛒
                <span id="cart-count" class="absolute -top-1 -right-1 bg-white text-orange-600 text-[10px] w-5 h-5 flex items-center justify-center rounded-full font-bold">0</span>
            </button>
        </div>
    </nav>

    <!-- Hero Section -->
    <header class="relative h-[70vh] flex items-center justify-center text-center">
        <img src="https://images.unsplash.com/photo-1687392946855-8e35efa25ad7?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080" 
             alt="Hero Background" 
             class="absolute inset-0 w-full h-full object-cover opacity-40">
        <div class="relative z-10 px-4">
            <h2 class="text-5xl md:text-7xl font-bold mb-6">Master Your Digital Presence</h2>
            <p class="text-xl text-slate-300 mb-8 max-w-2xl mx-auto">
                Elite growth strategies engineered for brands that demand performance, visibility, and measurable results.
            </p>
            <button class="px-8 py-3 bg-orange-600 hover:bg-orange-500 transition rounded-full font-bold shadow-lg shadow-orange-900/50">
                Explore Solutions
            </button>
        </div>
    </header>

    <!-- Product Packages Section -->
    <section class="container mx-auto py-20 px-6">
        <h2 class="text-4xl font-bold text-center mb-12">Premium Growth Packages</h2>
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8" id="product-grid">
            
            <!-- Item 1 -->
            <div class="glass p-6 rounded-3xl hover:border-orange-500 transition border border-transparent flex flex-col justify-between">
                <div>
                    <img src="https://images.unsplash.com/photo-1599930200736-01c254e529e8?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080" class="rounded-2xl mb-4 h-48 w-full object-cover" alt="IG Pro Growth">
                    <h3 class="text-xl font-bold">IG Pro Growth</h3>
                    <p class="text-slate-400 text-sm mb-4">High-intent organic engagement.</p>
                </div>
                <button onclick="addToCart('IG Pro Growth', 199)" class="w-full py-2 bg-slate-800 hover:bg-orange-600 rounded-lg transition">Add $199</button>
            </div>

            <!-- Item 2 -->
            <div class="glass p-6 rounded-3xl hover:border-orange-500 transition border border-transparent flex flex-col justify-between">
                <div>
                    <img src="https://images.unsplash.com/photo-1596346599094-4dfa5c61fd0d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080" class="rounded-2xl mb-4 h-48 w-full object-cover" alt="TikTok Viral">
                    <h3 class="text-xl font-bold">TikTok Viral</h3>
                    <p class="text-slate-400 text-sm mb-4">Fast-track to millions of views.</p>
                </div>
                <button onclick="addToCart('TikTok Viral', 249)" class="w-full py-2 bg-slate-800 hover:bg-orange-600 rounded-lg transition">Add $249</button>
            </div>

            <!-- Item 3 -->
            <div class="glass p-6 rounded-3xl hover:border-orange-500 transition border border-transparent flex flex-col justify-between">
                <div>
                    <img src="https://images.unsplash.com/photo-1560472354-b33ff0c44a43?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080" class="rounded-2xl mb-4 h-48 w-full object-cover" alt="YT Authority">
                    <h3 class="text-xl font-bold">YT Authority</h3>
                    <p class="text-slate-400 text-sm mb-4">Strategic channel development.</p>
                </div>
                <button onclick="addToCart('YT Authority', 299)" class="w-full py-2 bg-slate-800 hover:bg-orange-600 rounded-lg transition">Add $299</button>
            </div>

            <!-- Item 4 -->
            <div class="glass p-6 rounded-3xl hover:border-orange-500 transition border border-transparent flex flex-col justify-between">
                <div>
                    <img src="https://images.unsplash.com/photo-1560472354-b33ff0c44a43?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080" class="rounded-2xl mb-4 h-48 w-full object-cover" alt="X Presence">
                    <h3 class="text-xl font-bold">X Presence</h3>
                    <p class="text-slate-400 text-sm mb-4">Thought leadership and growth.</p>
                </div>
                <button onclick="addToCart('X Presence', 149)" class="w-full py-2 bg-slate-800 hover:bg-orange-600 rounded-lg transition">Add $149</button>
            </div>

        </div>
    </section>

    <!-- Toast Notification -->
    <div id="toast" class="fixed top-20 right-6 bg-orange-600 text-white px-6 py-3 rounded-lg shadow-xl translate-x-[200%] transition-transform duration-500 z-[100]">
        Added to cart!
    </div>

    <!-- Script -->
    <script>
        let cart = [];
        function addToCart(name, price) {
            cart.push({ name, price });
            document.getElementById('cart-count').innerText = cart.length;
            
            const t = document.getElementById('toast');
            t.classList.remove('translate-x-[200%]');
            
            setTimeout(() => {
                t.classList.add('translate-x-[200%]');
            }, 2000);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(STORE_HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
