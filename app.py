const HTML_TEMPLATE = `<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>أورا - الموضة الراقية</title>
    <!-- Cairo Font for Premium Arabic Typography -->
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Cairo', 'sans-serif'],
                    },
                    colors: {
                        primary: '#f97316', // Orange Accent
                    }
                }
            }
        }
    </script>
    <style>
        body {
            font-family: 'Cairo', sans-serif;
            background-color: #0b0b0c;
            color: #f4f4f5;
        }
        /* Custom scrollbars */
        ::-webkit-scrollbar {
            width: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #121214;
        }
        ::-webkit-scrollbar-thumb {
            background: #27272a;
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #f97316;
        }
    </style>
</head>
<body class="min-h-screen flex flex-col overflow-x-hidden">

    <!-- 1. Announcement Bar -->
    <div class="bg-primary text-black text-center py-2 px-4 text-xs font-semibold tracking-wide">
        شحن مجاني لكافة الطلبات بقيمة 300 ريال أو أكثر • كود الخصم: AURA10
    </div>

    <!-- 2. Sticky Glassmorphic Header -->
    <header class="sticky top-0 z-40 bg-zinc-950/80 backdrop-blur-md border-b border-zinc-900 px-4 py-3 lg:px-8">
        <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
            <!-- Brand Logo -->
            <div class="flex items-center gap-2">
                <span class="text-2xl font-bold tracking-tight text-white flex items-center gap-1">
                    أورا <span class="text-primary text-3xl font-light">.</span>
                </span>
            </div>

            <!-- Search Bar -->
            <div class="hidden md:flex flex-1 max-w-md mx-4">
                <div class="relative w-full">
                    <input type="text" id="searchInput" placeholder="ابحث عن منتجك المفضل..." 
                           class="w-full bg-zinc-900 border border-zinc-800 rounded-full py-1.5 px-4 pr-10 text-sm text-zinc-200 placeholder-zinc-500 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all">
                    <span class="absolute left-3 top-2.5 text-zinc-500 text-sm">🔍</span>
                </div>
            </div>

            <!-- Header Actions -->
            <div class="flex items-center gap-4">
                <button id="cartToggleBtn" class="relative p-2 text-zinc-300 hover:text-primary transition-colors focus:outline-none">
                    <span class="text-xl">🛒</span>
                    <span id="cartCountBadge" class="absolute -top-1 -right-1 bg-primary text-black font-bold text-[10px] w-5 h-5 rounded-full flex items-center justify-center border border-zinc-950">
                        0
                    </span>
                </button>
            </div>
        </div>
    </header>

    <!-- 3. Elegant Hero Section -->
    <section class="relative min-h-[500px] flex items-center justify-center py-16 px-4 bg-zinc-950 overflow-hidden">
        <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(249,115,22,0.1)_0,transparent_60%)]"></div>
        <div class="max-w-7xl mx-auto w-full grid grid-cols-1 lg:grid-cols-2 gap-12 items-center relative z-10">
            <!-- Text Content -->
            <div class="space-y-6 text-right">
                <span class="inline-block px-3 py-1 bg-primary/10 border border-primary/20 text-primary rounded-full text-xs font-semibold">
                    تشكيلة صيف 2026 الحصرية
                </span>
                <h1 class="text-4xl sm:text-5xl lg:text-6xl font-bold text-white leading-tight">
                    تأنق بالجاذبية الكلاسيكية والتصميم العصري
                </h1>
                <p class="text-zinc-400 text-base sm:text-lg max-w-xl font-light">
                    نقدم لك أرقى الملابس الرياضية المصممة بعناية فائقة لتلائم نشاطك اليومي وتمنحك أقصى درجات الثقة والراحة.
                </p>
                <div class="flex flex-wrap gap-4 pt-4 justify-start">
                    <a href="#products" class="bg-primary hover:bg-orange-600 text-black font-bold px-8 py-3 rounded-full transition-all duration-300 shadow-lg shadow-primary/20">
                        تسوق الآن
                    </a>
                </div>
            </div>
            <!-- Image Frame -->
            <div class="relative">
                <div class="absolute inset-0 bg-gradient-to-tr from-primary/20 to-transparent rounded-3xl blur-2xl"></div>
                <img src="https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=1200&q=80" 
                     alt="Aura Boutique Banner" 
                     class="w-full h-[350px] lg:h-[450px] object-cover rounded-3xl border border-zinc-800 shadow-2xl relative z-10">
            </div>
        </div>
    </section>

    <!-- Trust Badges -->
    <div class="border-y border-zinc-900 bg-zinc-950 py-8 px-4">
        <div class="max-w-7xl mx-auto grid grid-cols-2 lg:grid-cols-4 gap-6 text-center">
            <div class="space-y-2">
                <div class="text-3xl text-primary">🚚</div>
                <h3 class="text-sm font-bold text-white">شحن سريع وآمن</h3>
                <p class="text-xs text-zinc-500">توصيل لباب منزلك خلال 48 ساعة</p>
            </div>
            <div class="space-y-2">
                <div class="text-3xl text-primary">💵</div>
                <h3 class="text-sm font-bold text-white">الدفع عند الاستلام</h3>
                <p class="text-xs text-zinc-500">ادفع فقط عندما تستلم شحنتك</p>
            </div>
            <div class="space-y-2">
                <div class="text-3xl text-primary">🛡️</div>
                <h3 class="text-sm font-bold text-white">ضمان الجودة</h3>
                <p class="text-xs text-zinc-500">استرجاع مجاني خلال 14 يوماً</p>
            </div>
            <div class="space-y-2">
                <div class="text-3xl text-primary">💬</div>
                <h3 class="text-sm font-bold text-white">دعم متواصل 24/7</h3>
                <p class="text-xs text-zinc-500">نحن معك في كل خطوة للاستفسار</p>
            </div>
        </div>
    </div>

    <!-- 4. Filterable / Beautiful Product Grid -->
    <main id="products" class="max-w-7xl mx-auto px-4 py-16 flex-grow">
        <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12">
            <div>
                <h2 class="text-3xl font-bold text-white">منتجاتنا المختارة</h2>
                <p class="text-zinc-500 mt-1 text-sm">تسوق المنتجات الفاخرة الأعلى تقييماً</p>
            </div>
            <div class="flex gap-2 self-start md:self-auto overflow-x-auto pb-2 w-full md:w-auto">
                <button onclick="filterProducts('all')" class="bg-primary text-black px-5 py-1.5 rounded-full text-xs font-bold whitespace-nowrap transition-colors">الكل</button>
                <button onclick="filterProducts('shoes')" class="bg-zinc-900 text-zinc-400 hover:text-white px-5 py-1.5 rounded-full text-xs font-semibold whitespace-nowrap transition-colors">أحذية رياضة</button>
                <button onclick="filterProducts('apparel')" class="bg-zinc-900 text-zinc-400 hover:text-white px-5 py-1.5 rounded-full text-xs font-semibold whitespace-nowrap transition-colors">ملابس أنيقة</button>
            </div>
        </div>

        <div id="productGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            <!-- Product Card 1 -->
            <div class="group bg-zinc-950 border border-zinc-900 rounded-2xl overflow-hidden hover:border-zinc-800 transition-all duration-300 flex flex-col" data-category="shoes">
                <div class="relative overflow-hidden aspect-square">
                    <span class="absolute top-3 right-3 bg-primary text-black text-[10px] font-bold px-2.5 py-1 rounded-full z-10 shadow-lg">-20%خصم</span>
                    <img src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=600&q=80" 
                         alt="Classic Runner 1.0" 
                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                </div>
                <div class="p-5 flex-grow flex flex-col justify-between">
                    <div>
                        <div class="flex items-center gap-1 text-yellow-500 text-xs mb-1">★★★★★ <span class="text-zinc-500 text-[10px] mr-1">(4.9)</span></div>
                        <h3 class="font-bold text-white text-base">حذاء كلاسيك رانر البرتقالي</h3>
                        <p class="text-zinc-500 text-xs mt-1 font-light">نسيج خفيف ومريح للغاية مخصص للمسافات الطويلة.</p>
                    </div>
                    <div class="flex items-center justify-between mt-5 pt-3 border-t border-zinc-900/50">
                        <div>
                            <span class="text-primary font-bold text-base">299 ريال</span>
                            <span class="text-zinc-600 line-through text-xs block">379 ريال</span>
                        </div>
                        <button onclick="addToCart('حذاء كلاسيك رانر البرتقالي', 299, 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=150&q=80')" 
                                class="bg-primary hover:bg-orange-600 text-black font-semibold text-xs py-2 px-4 rounded-full transition-colors">
                            إضافة للسلّة
                        </button>
                    </div>
                </div>
            </div>

            <!-- Product Card 2 -->
            <div class="group bg-zinc-950 border border-zinc-900 rounded-2xl overflow-hidden hover:border-zinc-800 transition-all duration-300 flex flex-col" data-category="apparel">
                <div class="relative overflow-hidden aspect-square">
                    <img src="https://images.unsplash.com/photo-1434389677669-e08b4cac3105?auto=format&fit=crop&w=600&q=80" 
                         alt="Tech Hoodie" 
                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                </div>
                <div class="p-5 flex-grow flex flex-col justify-between">
                    <div>
                        <div class="flex items-center gap-1 text-yellow-500 text-xs mb-1">★★★★★ <span class="text-zinc-500 text-[10px] mr-1">(4.8)</span></div>
                        <h3 class="font-bold text-white text-base">سترة تيك هودي العصرية</h3>
                        <p class="text-zinc-500 text-xs mt-1 font-light">خامة قطنية فاخرة مقاومة للتعرق ومثالية للأنشطة والرياضة.</p>
                    </div>
                    <div class="flex items-center justify-between mt-5 pt-3 border-t border-zinc-900/50">
                        <div>
                            <span class="text-primary font-bold text-base">189 ريال</span>
                        </div>
                        <button onclick="addToCart('سترة تيك هودي العصرية', 189, 'https://images.unsplash.com/photo-1434389677669-e08b4cac3105?auto=format&fit=crop&w=150&q=80')" 
                                class="bg-primary hover:bg-orange-600 text-black font-semibold text-xs py-2 px-4 rounded-full transition-colors">
                            إضافة للسلّة
                        </button>
                    </div>
                </div>
            </div>

            <!-- Product Card 3 -->
            <div class="group bg-zinc-950 border border-zinc-900 rounded-2xl overflow-hidden hover:border-zinc-800 transition-all duration-300 flex flex-col" data-category="shoes">
                <div class="relative overflow-hidden aspect-square">
                    <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=600&q=80" 
                         alt="Minimalist Chrono Watch" 
                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                </div>
                <div class="p-5 flex-grow flex flex-col justify-between">
                    <div>
                        <div class="flex items-center gap-1 text-yellow-500 text-xs mb-1">★★★★★ <span class="text-zinc-500 text-[10px] mr-1">(5.0)</span></div>
                        <h3 class="font-bold text-white text-base">ساعة أورا بورتوفينو الفاخرة</h3>
                        <p class="text-zinc-500 text-xs mt-1 font-light">قرص ساعة عتيق مع حزام جلدي طبيعي فاخر مقاوم للماء.</p>
                    </div>
                    <div class="flex items-center justify-between mt-5 pt-3 border-t border-zinc-900/50">
                        <div>
                            <span class="text-primary font-bold text-base">450 ريال</span>
                        </div>
                        <button onclick="addToCart('ساعة أورا بورتوفينو الفاخرة', 450, 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=150&q=80')" 
                                class="bg-primary hover:bg-orange-600 text-black font-semibold text-xs py-2 px-4 rounded-full transition-colors">
                            إضافة للسلّة
                        </button>
                    </div>
                </div>
            </div>

            <!-- Product Card 4 -->
            <div class="group bg-zinc-950 border border-zinc-900 rounded-2xl overflow-hidden hover:border-zinc-800 transition-all duration-300 flex flex-col" data-category="apparel">
                <div class="relative overflow-hidden aspect-square">
                    <span class="absolute top-3 right-3 bg-red-600 text-white text-[10px] font-bold px-2.5 py-1 rounded-full z-10 shadow-lg">جديد</span>
                    <img src="https://images.unsplash.com/photo-1483985988355-763728e1935b?auto=format&fit=crop&w=600&q=80" 
                         alt="Signature Coat" 
                         class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                </div>
                <div class="p-5 flex-grow flex flex-col justify-between">
                    <div>
                        <div class="flex items-center gap-1 text-yellow-500 text-xs mb-1">★★★★★ <span class="text-zinc-500 text-[10px] mr-1">(4.7)</span></div>
                        <h3 class="font-bold text-white text-base">سترة الفصول الأربعة الأنيقة</h3>
                        <p class="text-zinc-500 text-xs mt-1 font-light">قصة كلاسيكية فخمة وخامات متطورة تحمي من البرد والمطر.</p>
                    </div>
                    <div class="flex items-center justify-between mt-5 pt-3 border-t border-zinc-900/50">
                        <div>
                            <span class="text-primary font-bold text-base">320 ريال</span>
                        </div>
                        <button onclick="addToCart('سترة الفصول الأربعة الأنيقة', 320, 'https://images.unsplash.com/photo-1483985988355-763728e1935b?auto=format&fit=crop&w=150&q=80')" 
                                class="bg-primary hover:bg-orange-600 text-black font-semibold text-xs py-2 px-4 rounded-full transition-colors">
                            إضافة للسلّة
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <!-- 5. Social Proof: Customer Testimonials -->
    <section class="bg-zinc-950/60 border-t border-zinc-900 py-16 px-4">
        <div class="max-w-7xl mx-auto">
            <div class="text-center mb-12">
                <h2 class="text-2xl sm:text-3xl font-bold text-white">شركاء النجاح يعبرون عن رضاهم</h2>
                <p class="text-zinc-500 text-sm mt-1">قصص نجاح من عملاء فخورين بارتداء تصاميمنا</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Testimonial 1 -->
                <div class="bg-zinc-900/40 border border-zinc-900 p-6 rounded-2xl flex flex-col justify-between">
                    <p class="text-zinc-300 text-sm font-light leading-relaxed">"لقد بهرت بجودة النسيج وملاءمته التامة للجسم، والتوصيل كان أسرع مما توقعت في الرياض."</p>
                    <div class="flex items-center gap-3 mt-6">
                        <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=100&q=80" alt="سليمان العتيبي" class="w-10 h-10 rounded-full object-cover border border-primary/20">
                        <div>
                            <h4 class="text-xs font-bold text-white">سليمان العتيبي</h4>
                            <span class="text-[10px] text-zinc-500">عميل مؤكد من الرياض</span>
                        </div>
                    </div>
                </div>
                <!-- Testimonial 2 -->
                <div class="bg-zinc-900/40 border border-zinc-900 p-6 rounded-2xl flex flex-col justify-between">
                    <p class="text-zinc-300 text-sm font-light leading-relaxed">"تصاميم رائعة تدمج الموضة بالخامات الرياضية الثقيلة. المتجر ممتاز وسهل الاستخدام والتعامل."</p>
                    <div class="flex items-center gap-3 mt-6">
                        <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=100&q=80" alt="نورة القحطاني" class="w-10 h-10 rounded-full object-cover border border-primary/20">
                        <div>
                            <h4 class="text-xs font-bold text-white">نورة القحطاني</h4>
                            <span class="text-[10px] text-zinc-500">عميلة مؤكدة من جدة</span>
                        </div>
                    </div>
                </div>
                <!-- Testimonial 3 -->
                <div class="bg-zinc-900/40 border border-zinc-900 p-6 rounded-2xl flex flex-col justify-between">
                    <p class="text-zinc-300 text-sm font-light leading-relaxed">"ساعة اليد تضفي فخامة واضحة، تفاصيل الصناعة عالية والخدمة كانت استثنائية للغاية."</p>
                    <div class="flex items-center gap-3 mt-6">
                        <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=100&q=80" alt="خالد الحربي" class="w-10 h-10 rounded-full object-cover border border-primary/20">
                        <div>
                            <h4 class="text-xs font-bold text-white">خالد الحربي</h4>
                            <span class="text-[10px] text-zinc-500">عميل مؤكد من الشرقية</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 6. Interactive FAQ Accordion -->
    <section class="max-w-4xl mx-auto px-4 py-16">
        <h2 class="text-2xl sm:text-3xl font-bold text-white text-center mb-8">الأسئلة الشائعة</h2>
        <div class="space-y-4">
            <div class="border border-zinc-900 rounded-xl bg-zinc-950 overflow-hidden">
                <button onclick="toggleFaq(this)" class="w-full flex justify-between items-center p-5 text-right font-medium text-white hover:text-primary transition-colors focus:outline-none">
                    <span>كم يستغرق الشحن للطلبات؟</span>
                    <span class="faq-icon text-zinc-500">＋</span>
                </button>
                <div class="faq-content hidden p-5 pt-0 border-t border-zinc-900 text-sm text-zinc-400 font-light leading-relaxed">
                    يستغرق الشحن داخل المملكة العربية السعودية من 24 إلى 48 ساعة فقط، وخارجها من 3 إلى 5 أيام عمل.
                </div>
            </div>
            <div class="border border-zinc-900 rounded-xl bg-zinc-950 overflow-hidden">
                <button onclick="toggleFaq(this)" class="w-full flex justify-between items-center p-5 text-right font-medium text-white hover:text-primary transition-colors focus:outline-none">
                    <span>هل يدعم المتجر الدفع عند الاستلام (COD)؟</span>
                    <span class="faq-icon text-zinc-500">＋</span>
                </button>
                <div class="faq-content hidden p-5 pt-0 border-t border-zinc-900 text-sm text-zinc-400 font-light leading-relaxed">
                    نعم، نتيح لك الدفع عند استلام شحنتك نقداً أو بواسطة بطاقة مدى الائتمانية لزيادة مستويات الأمان والراحة.
                </div>
            </div>
        </div>
    </section>

    <!-- 7. Footer -->
    <footer class="bg-zinc-950 border-t border-zinc-900 py-12 px-4 mt-auto">
        <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8 mb-8 text-right">
            <div class="space-y-4">
                <span class="text-xl font-bold text-white">أورا .</span>
                <p class="text-zinc-500 text-xs font-light leading-relaxed">توفير الملابس والأحذية الفاخرة المستوحاة من الطراز العالمي لرفع جودة المعيشة اليومية.</p>
            </div>
            <div>
                <h4 class="text-white font-bold text-sm mb-4">روابط سريعة</h4>
                <ul class="space-y-2 text-zinc-500 text-xs">
                    <li><a href="#" class="hover:text-primary">الرئيسية</a></li>
                    <li><a href="#products" class="hover:text-primary">المنتجات الأكثر مبيعاً</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white font-bold text-sm mb-4">روابط الدعم</h4>
                <ul class="space-y-2 text-zinc-500 text-xs">
                    <li><a href="#" class="hover:text-primary">سياسة الخصوصية واسترجاع المشتريات</a></li>
                    <li><a href="#" class="hover:text-primary">الشروط والأحكام العامة</a></li>
                </ul>
            </div>
            <div class="space-y-3">
                <h4 class="text-white font-bold text-sm">تسوق بأمان تام</h4>
                <div class="flex gap-2 flex-wrap">
                    <span class="bg-zinc-900 text-zinc-300 text-[10px] px-2.5 py-1 rounded">Mada مدى</span>
                    <span class="bg-zinc-900 text-zinc-300 text-[10px] px-2.5 py-1 rounded">Visa</span>
                    <span class="bg-zinc-900 text-zinc-300 text-[10px] px-2.5 py-1 rounded">الدفع عند الاستلام</span>
                </div>
            </div>
        </div>
        <div class="max-w-7xl mx-auto border-t border-zinc-900 pt-6 text-center text-zinc-600 text-[11px]">
            &copy; 2026 متجر أورا التجاري. كافة الحقوق محفوظة.
        </div>
    </footer>

    <!-- SLIDE-OVER INTERACTIVE CART DRAWER -->
    <div id="cartDrawer" class="fixed inset-0 z-50 overflow-hidden hidden" aria-labelledby="slide-over-title" role="dialog" aria-modal="true">
        <div class="absolute inset-0 overflow-hidden">
            <div id="cartOverlay" class="absolute inset-0 bg-black/80 backdrop-blur-sm transition-opacity"></div>
            <div class="pointer-events-none fixed inset-y-0 left-0 flex max-w-full pr-10">
                <div class="pointer-events-auto w-screen max-w-md bg-zinc-950 border-r border-zinc-900 flex flex-col">
                    <div class="px-4 py-6 sm:px-6 border-b border-zinc-900 flex items-center justify-between">
                        <h2 class="text-lg font-bold text-white flex items-center gap-2">
                            حقيبة تسوقك <span id="cartCountLabel" class="text-xs bg-primary/20 text-primary px-2 py-0.5 rounded-full">0 عناصر</span>
                        </h2>
                        <button id="cartCloseBtn" class="text-zinc-500 hover:text-white text-xl p-1 focus:outline-none">✕</button>
                    </div>
                    <div class="flex-1 overflow-y-auto px-4 py-6 sm:px-6">
                        <div id="cartItemsList" class="space-y-6">
                            <div id="cartEmptyPlaceholder" class="text-center py-16 space-y-4">
                                <span class="text-5xl block">🛍️</span>
                                <p class="text-zinc-500 text-xs">سلتك لا تزال فارغة حالياً</p>
                            </div>
                        </div>
                    </div>
                    <div class="border-t border-zinc-900 px-4 py-6 sm:px-6 bg-zinc-900/10 space-y-4">
                        <div class="flex justify-between text-base font-medium text-white">
                            <span>المجموع الكلي:</span>
                            <span id="cartTotalPrice" class="text-primary font-bold">0 ريال</span>
                        </div>
                        <p class="text-[10px] text-zinc-500">تم احتساب رسوم الشحن والضرائب تلقائياً بخصم الشحن المجاني.</p>
                        <button id="checkoutBtn" class="w-full bg-primary hover:bg-orange-600 text-black font-bold py-3 rounded-xl transition-all duration-300">
                            إتمام الطلب (الدفع عند الاستلام)
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- CASH ON DELIVERY CHECKOUT FORM MODAL -->
    <div id="checkoutModal" class="fixed inset-0 z-50 overflow-y-auto hidden flex items-center justify-center p-4">
        <div id="checkoutOverlay" class="fixed inset-0 bg-black/90 backdrop-blur-md"></div>
        <div class="relative bg-zinc-950 border border-zinc-900 w-full max-w-lg rounded-2xl overflow-hidden p-6 sm:p-8 z-10 space-y-6">
            <div class="flex justify-between items-center border-b border-zinc-900 pb-4">
                <h3 class="text-xl font-bold text-white">شحن وتأكيد طلبك (COD)</h3>
                <button id="closeCheckoutBtn" class="text-zinc-500 hover:text-white text-lg">✕</button>
            </div>
            <div class="flex items-center justify-between text-xs text-zinc-500 border-b border-zinc-900 pb-4">
                <div class="text-primary font-semibold">1. بيانات التوصيل</div>
                <div>➔</div>
                <div>2. تأكيد وشحن الطلب</div>
            </div>
            <form id="codForm" onsubmit="handleCheckoutSubmit(event)" class="space-y-4">
                <div class="space-y-1">
                    <label class="text-xs text-zinc-400 font-medium">الاسم الكامل لمتلقي الشحنة *</label>
                    <input type="text" required placeholder="مثال: سلمان العتيبي" class="w-full bg-zinc-900 border border-zinc-800 rounded-lg py-2 px-3 text-sm focus:outline-none focus:border-primary text-white">
                </div>
                <div class="space-y-1">
                    <label class="text-xs text-zinc-400 font-medium">رقم الجوال الفعال (للتأكيد قبل الشحن) *</label>
                    <input type="tel" required placeholder="مثال: 05XXXXXXXX" class="w-full bg-zinc-900 border border-zinc-800 rounded-lg py-2 px-3 text-sm focus:outline-none focus:border-primary text-white">
                </div>
                <div class="space-y-1">
                    <label class="text-xs text-zinc-400 font-medium">المدينة الحالية *</label>
                    <input type="text" required placeholder="مثال: الرياض" class="w-full bg-zinc-900 border border-zinc-800 rounded-lg py-2 px-3 text-sm focus:outline-none focus:border-primary text-white">
                </div>
                <div class="space-y-1">
                    <label class="text-xs text-zinc-400 font-medium">العنوان التفصيلي والحي للشارع *</label>
                    <input type="text" required placeholder="مثال: حي الياسمين، شارع العليا" class="w-full bg-zinc-900 border border-zinc-800 rounded-lg py-2 px-3 text-sm focus:outline-none focus:border-primary text-white">
                </div>
                <div class="pt-4 flex items-center justify-between border-t border-zinc-900">
                    <span id="modalCheckoutTotal" class="text-base font-bold text-primary">المجموع: 0 ريال</span>
                    <button type="submit" class="bg-primary hover:bg-orange-600 text-black font-bold px-6 py-2.5 rounded-lg transition-colors text-sm">
                        تأكيد وإتمام الشراء
                    </button>
                </div>
            </form>
        </div>
    </div>

    <!-- CUSTOM FLOATING TOAST NOTIFICATIONS (NO ALERTS) -->
    <div id="toastContainer" class="fixed top-6 right-6 z-50 flex flex-col gap-3 pointer-events-none"></div>

    <!-- INLINE CART INTERACTIVITY JAVASCRIPT -->
    <script>
        // Store Local Cart State
        let cart = [];

        // Custom Toast Notification System
        function showToast(message, type = 'success') {
            const container = document.getElementById('toastContainer');
            const toast = document.createElement('div');
            toast.className = 'pointer-events-auto bg-zinc-900 border border-zinc-800 px-4 py-3 rounded-xl flex items-center gap-3 shadow-2xl transition-all duration-300 transform translate-x-12 opacity-0 text-xs text-white max-w-sm';
            
            const icon = type === 'success' ? '✅' : 'ℹ️';
            toast.innerHTML = \`
                <span>\${icon}</span>
                <div class="flex-grow font-medium">\${message}</div>
                <button onclick="this.parentElement.remove()" class="text-zinc-600 hover:text-zinc-400 ml-1">✕</button>
            \`;
            container.appendChild(toast);
            
            setTimeout(() => {
                toast.classList.remove('translate-x-12', 'opacity-0');
            }, 10);

            setTimeout(() => {
                toast.classList.add('translate-x-12', 'opacity-0');
                setTimeout(() => toast.remove(), 300);
            }, 4000);
        }

        // Toggle FAQ Accordions
        function toggleFaq(btn) {
            const content = btn.nextElementSibling;
            const icon = btn.querySelector('.faq-icon');
            const isHidden = content.classList.contains('hidden');
            
            document.querySelectorAll('.faq-content').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.faq-icon').forEach(el => el.textContent = '＋');

            if (isHidden) {
                content.classList.remove('hidden');
                icon.textContent = '－';
            }
        }

        // Filter Products in Grid
        function filterProducts(category) {
            const cards = document.querySelectorAll('#productGrid > div');
            cards.forEach(card => {
                if (category === 'all' || card.getAttribute('data-category') === category) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });

            // Update active filter button styling
            const buttons = document.querySelectorAll('#products button[onclick^="filterProducts"]');
            buttons.forEach(btn => {
                if (btn.getAttribute('onclick').includes(\`'\${category}'\`)) {
                    btn.className = 'bg-primary text-black px-5 py-1.5 rounded-full text-xs font-bold whitespace-nowrap transition-colors';
                } else {
                    btn.className = 'bg-zinc-900 text-zinc-400 hover:text-white px-5 py-1.5 rounded-full text-xs font-semibold whitespace-nowrap transition-colors';
                }
            });
        }

        // Add Product to Cart
        function addToCart(title, price, image) {
            const existingItem = cart.find(item => item.title === title);
            if (existingItem) {
                existingItem.quantity += 1;
            } else {
                cart.push({ title, price, image, quantity: 1 });
            }
            updateCartUI();
            showToast(\`تمت إضافة "\${title}" إلى السلة بنجاح\`);
        }

        // Update Cart UI Elements
        function updateCartUI() {
            const cartItemsList = document.getElementById('cartItemsList');
            const cartCountBadge = document.getElementById('cartCountBadge');
            const cartCountLabel = document.getElementById('cartCountLabel');
            const cartTotalPrice = document.getElementById('cartTotalPrice');
            const modalCheckoutTotal = document.getElementById('modalCheckoutTotal');

            const totalCount = cart.reduce((sum, item) => sum + item.quantity, 0);
            const totalSum = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);

            cartCountBadge.textContent = totalCount;
            cartCountLabel.textContent = \`\${totalCount} عناصر\`;
            cartTotalPrice.textContent = \`\${totalSum} ريال\`;
            if (modalCheckoutTotal) {
                modalCheckoutTotal.textContent = \`المجموع: \${totalSum} ريال\`;
            }

            if (cart.length === 0) {
                cartItemsList.innerHTML = \`
                    <div id="cartEmptyPlaceholder" class="text-center py-16 space-y-4">
                        <span class="text-5xl block">🛍️</span>
                        <p class="text-zinc-500 text-xs">سلتك لا تزال فارغة حالياً</p>
                    </div>
                \`;
                return;
            }

            cartItemsList.innerHTML = cart.map((item, index) => \`
                <div class="flex items-center justify-between gap-4 border-b border-zinc-900 pb-4">
                    <img src="\${item.image}" alt="\${item.title}" class="w-16 h-16 object-cover rounded-xl border border-zinc-800">
                    <div class="flex-1">
                        <h4 class="text-xs font-bold text-white line-clamp-1">\${item.title}</h4>
                        <p class="text-xs text-primary font-semibold mt-1">\${item.price} ريال</p>
                        <div class="flex items-center gap-2 mt-2">
                            <button onclick="updateQuantity(\${index}, -1)" class="w-6 h-6 bg-zinc-900 text-zinc-300 rounded hover:bg-zinc-800 text-xs font-bold">-</button>
                            <span class="text-xs text-white px-2 font-bold">\${item.quantity}</span>
                            <button onclick="updateQuantity(\${index}, 1)" class="w-6 h-6 bg-zinc-900 text-zinc-300 rounded hover:bg-zinc-800 text-xs font-bold">+</button>
                        </div>
                    </div>
                    <button onclick="removeFromCart(\${index})" class="text-zinc-600 hover:text-red-500 text-sm p-1">🗑️</button>
                </div>
            \`).join('');
        }

        // Update Item Quantity
        function updateQuantity(index, change) {
            if (cart[index]) {
                cart[index].quantity += change;
                if (cart[index].quantity <= 0) {
                    cart.splice(index, 1);
                }
                updateCartUI();
            }
        }

        // Remove Item from Cart
        function removeFromCart(index) {
            if (cart[index]) {
                showToast(\`تم حذف "\${cart[index].title}" من السلة\`, 'info');
                cart.splice(index, 1);
                updateCartUI();
            }
        }

        // Drawer Controls
        const cartDrawer = document.getElementById('cartDrawer');
        const cartToggleBtn = document.getElementById('cartToggleBtn');
        const cartCloseBtn = document.getElementById('cartCloseBtn');
        const cartOverlay = document.getElementById('cartOverlay');

        function openCart() { cartDrawer.classList.remove('hidden'); }
        function closeCart() { cartDrawer.classList.add('hidden'); }

        cartToggleBtn.addEventListener('click', openCart);
        cartCloseBtn.addEventListener('click', closeCart);
        cartOverlay.addEventListener('click', closeCart);

        // Checkout Modal Controls
        const checkoutModal = document.getElementById('checkoutModal');
        const checkoutBtn = document.getElementById('checkoutBtn');
        const closeCheckoutBtn = document.getElementById('closeCheckoutBtn');
        const checkoutOverlay = document.getElementById('checkoutOverlay');

        checkoutBtn.addEventListener('click', () => {
            if (cart.length === 0) {
                showToast('السلة فارغة! أضف بعض المنتجات أولاً.', 'info');
                return;
            }
            closeCart();
            checkoutModal.classList.remove('hidden');
        });

        function closeCheckout() { checkoutModal.classList.add('hidden'); }
        closeCheckoutBtn.addEventListener('click', closeCheckout);
        checkoutOverlay.addEventListener('click', closeCheckout);

        // Handle Order Submission
        function handleCheckoutSubmit(event) {
            event.preventDefault();
            showToast('تم استلام طلبك بنجاح! سنتصل بك قريباً للتأكيد.', 'success');
            cart = [];
            updateCartUI();
            closeCheckout();
        }

        // Live Product Search Filter
        const searchInput = document.getElementById('searchInput');
        if (searchInput) {
            searchInput.addEventListener('input', (e) => {
                const term = e.target.value.toLowerCase().trim();
                const cards = document.querySelectorAll('#productGrid > div');
                cards.forEach(card => {
                    const title = card.querySelector('h3').textContent.toLowerCase();
                    if (title.includes(term)) {
                        card.style.display = 'flex';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        }
    </script>
</body>
</html>\`;
