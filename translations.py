# -*- coding: utf-8 -*-
"""
PlantGuard AI — Multilingual Translation Module
================================================
Provides UI strings and treatment data in three languages:
  • English (en)
  • French  (fr)
  • Arabic  (ar)  — Modern Standard Arabic accessible to North African farmers

Usage:
    from translations import tr, get_treatments, set_lang

    set_lang("fr")
    print(tr("window_title"))
    info = get_treatments("Tomato___Early_blight")
"""

# ---------------------------------------------------------------------------
# Module-level state
# ---------------------------------------------------------------------------
current_lang = "en"
SUPPORTED_LANGS = {"en": "English", "fr": "Français", "ar": "العربية"}

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def set_lang(lang):
    """Set the active language. *lang* must be a key in SUPPORTED_LANGS."""
    global current_lang
    if lang in SUPPORTED_LANGS:
        current_lang = lang


def get_lang():
    """Return the current language code."""
    return current_lang


def tr(key):
    """Return the UI string for *key* in the current language."""
    return UI_STRINGS.get(current_lang, UI_STRINGS["en"]).get(
        key, UI_STRINGS["en"].get(key, key)
    )


def get_treatments(class_name):
    """Return the treatment dict for *class_name* in the current language."""
    lang_treatments = TREATMENTS_I18N.get(current_lang, TREATMENTS_I18N["en"])
    return lang_treatments.get(class_name, None)


# ╔═════════════════════════════════════════════════════════════════════════╗
# ║                          UI  S T R I N G S                            ║
# ╚═════════════════════════════════════════════════════════════════════════╝

UI_STRINGS = {
    # ── English ───────────────────────────────────────────────────────────
    "en": {
        "window_title": "PlantGuard AI — Disease Detection",
        "app_name": "PlantGuard AI",
        "app_subtitle": "Plant Disease Detection System",
        "status_checking": "Checking files...",
        "status_ready": "Ready — 12 classes (Corn / Grape / Tomato)",
        "status_missing": "Missing: {items}",
        "upload_label": "Upload Leaf Image",
        "drop_placeholder": (
            "\n\n\nDrop leaf image here\n\nor click to browse\n\n"
            "Supported: JPG, PNG"
        ),
        "btn_analyse": "Analyse Disease",
        "btn_reset": "Reset",
        "ready_title": "Ready to Analyse",
        "ready_desc": (
            "Upload a leaf image on the left\n"
            "and click Analyse Disease"
        ),
        "supported_title": "Supported Plants Only:",
        "supported_list": (
            "Corn (maize)  |  Grapevine  |  Tomato\n"
            "For best results: use clear, well-lit leaf photos"
        ),
        "loading": "Analysing leaf image, please wait...",
        "confidence": "Confidence:",
        "top_predictions": "Top Predictions:",
        "status_healthy": "[Healthy]",
        "status_disease": "[Disease Detected]",
        "healthy_msg": (
            "This plant appears healthy!\n"
            "No disease treatment required."
        ),
        "natural_title": "Natural Treatment",
        "chemical_title": "Chemical Treatment",
        "preventive_title": "Preventive Care Tips",
        "low_conf_title": "Low Confidence — Result may be incorrect",
        "low_conf_desc": (
            "The image may not match any supported plant.\n"
            "Please use a clear, well-lit photo of a Corn, Grape or Tomato leaf."
        ),
        "mod_conf_title": "Moderate Confidence — Verify with an expert",
        "error_prefix": "Error:",
        "file_dialog_title": "Select Leaf Image",
    },

    # ── French ────────────────────────────────────────────────────────────
    "fr": {
        "window_title": "PlantGuard AI — Détection des Maladies",
        "app_name": "PlantGuard AI",
        "app_subtitle": "Système de Détection des Maladies des Plantes",
        "status_checking": "Vérification des fichiers...",
        "status_ready": "Prêt — 12 classes (Maïs / Vigne / Tomate)",
        "status_missing": "Manquant : {items}",
        "upload_label": "Télécharger l'image de feuille",
        "drop_placeholder": (
            "\n\n\nDéposez l'image de feuille ici\n\n"
            "ou cliquez pour parcourir\n\n"
            "Formats supportés : JPG, PNG"
        ),
        "btn_analyse": "Analyser la maladie",
        "btn_reset": "Réinitialiser",
        "ready_title": "Prêt pour l'analyse",
        "ready_desc": (
            "Téléchargez une image de feuille à gauche\n"
            "et cliquez sur Analyser la maladie"
        ),
        "supported_title": "Plantes prises en charge uniquement :",
        "supported_list": (
            "Maïs  |  Vigne  |  Tomate\n"
            "Pour de meilleurs résultats : utilisez des photos de feuilles claires et bien éclairées"
        ),
        "loading": "Analyse de l'image en cours, veuillez patienter...",
        "confidence": "Confiance :",
        "top_predictions": "Prédictions principales :",
        "status_healthy": "[Saine]",
        "status_disease": "[Maladie détectée]",
        "healthy_msg": (
            "Cette plante semble saine !\n"
            "Aucun traitement nécessaire."
        ),
        "natural_title": "Traitement naturel",
        "chemical_title": "Traitement chimique",
        "preventive_title": "Conseils de prévention",
        "low_conf_title": "Confiance faible — Le résultat peut être incorrect",
        "low_conf_desc": (
            "L'image peut ne pas correspondre à une plante prise en charge.\n"
            "Veuillez utiliser une photo claire et bien éclairée d'une feuille de Maïs, Vigne ou Tomate."
        ),
        "mod_conf_title": "Confiance modérée — À vérifier avec un expert",
        "error_prefix": "Erreur :",
        "file_dialog_title": "Sélectionner une image de feuille",
    },

    # ── Arabic ────────────────────────────────────────────────────────────
    "ar": {
        "window_title": "PlantGuard AI — كشف أمراض النباتات",
        "app_name": "PlantGuard AI",
        "app_subtitle": "نظام كشف أمراض النباتات",
        "status_checking": "جارٍ فحص الملفات...",
        "status_ready": "جاهز — 12 صنفًا (ذرة / عنب / طماطم)",
        "status_missing": "ملفات ناقصة: {items}",
        "upload_label": "تحميل صورة الورقة",
        "drop_placeholder": (
            "\n\n\nأسقِط صورة الورقة هنا\n\n"
            "أو انقر للتصفّح\n\n"
            "الصيغ المدعومة: JPG، PNG"
        ),
        "btn_analyse": "تحليل المرض",
        "btn_reset": "إعادة تعيين",
        "ready_title": "جاهز للتحليل",
        "ready_desc": (
            "حمّل صورة ورقة النبات على اليسار\n"
            "ثم اضغط على تحليل المرض"
        ),
        "supported_title": "النباتات المدعومة فقط:",
        "supported_list": (
            "الذرة  |  العنب  |  الطماطم\n"
            "للحصول على أفضل النتائج: استخدم صورًا واضحة وجيدة الإضاءة للأوراق"
        ),
        "loading": "جارٍ تحليل صورة الورقة، يرجى الانتظار...",
        "confidence": "نسبة الثقة:",
        "top_predictions": "أعلى التوقعات:",
        "status_healthy": "[سليمة]",
        "status_disease": "[تم اكتشاف مرض]",
        "healthy_msg": (
            "يبدو أن هذا النبات سليم!\n"
            "لا حاجة لأي علاج."
        ),
        "natural_title": "العلاج الطبيعي",
        "chemical_title": "العلاج الكيميائي",
        "preventive_title": "نصائح الوقاية",
        "low_conf_title": "ثقة منخفضة — قد تكون النتيجة غير دقيقة",
        "low_conf_desc": (
            "قد لا تتطابق الصورة مع أي نبات مدعوم.\n"
            "يرجى استخدام صورة واضحة وجيدة الإضاءة لورقة ذرة أو عنب أو طماطم."
        ),
        "mod_conf_title": "ثقة متوسطة — يُرجى التحقق مع خبير",
        "error_prefix": "خطأ:",
        "file_dialog_title": "اختيار صورة ورقة",
    },
}

# ╔═════════════════════════════════════════════════════════════════════════╗
# ║                    T R E A T M E N T S   I 1 8 N                     ║
# ╚═════════════════════════════════════════════════════════════════════════╝

TREATMENTS_I18N = {
    # ======================================================================
    #  E N G L I S H
    # ======================================================================
    "en": {
        # ── Corn ──────────────────────────────────────────────────────────
        "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
            "display": "Corn — Cercospora Leaf Spot",
            "plant": "Corn (Maize)",
            "disease": "Cercospora Leaf Spot / Gray Leaf Spot",
            "natural": [
                "Rotate crops every 2 years to break disease cycle",
                "Remove and destroy infected plant debris after harvest",
                "Spray diluted Neem oil (2%) every 7-10 days",
                "Ensure proper plant spacing for air circulation",
                "Avoid overhead irrigation — use drip irrigation",
            ],
            "chemical": [
                "Azoxystrobin (Amistar 250 SC) — apply at first symptoms",
                "Propiconazole (Tilt 250 EC) — 0.5 ml/L every 14 days",
                "Mancozeb (Dithane M-45) — 2.5 g/L preventive spray",
                "Pyraclostrobin (Cabrio Top) — foliar application",
            ],
        },
        "Corn_(maize)___Common_rust_": {
            "display": "Corn — Common Rust",
            "plant": "Corn (Maize)",
            "disease": "Common Rust (Puccinia sorghi)",
            "natural": [
                "Plant rust-resistant corn hybrid varieties",
                "Early planting to avoid peak rust season",
                "Remove volunteer corn plants around fields",
                "Apply potassium silicate spray to strengthen leaves",
                "Crop rotation with non-host plants (soybeans, wheat)",
            ],
            "chemical": [
                "Propiconazole (Tilt 250 EC) — apply at early infection",
                "Azoxystrobin + Propiconazole (Quilt Xcel) — systemic",
                "Trifloxystrobin (Flint 50 WG) — preventive application",
                "Tebuconazole (Folicur 250 EW) — 1 ml/L, 2 applications",
            ],
        },
        "Corn_(maize)___Northern_Leaf_Blight": {
            "display": "Corn — Northern Leaf Blight",
            "plant": "Corn (Maize)",
            "disease": "Northern Leaf Blight (Exserohilum turcicum)",
            "natural": [
                "Use resistant hybrid varieties (Ht gene resistance)",
                "Deep plow to bury infected crop residue",
                "Crop rotation (avoid corn-after-corn)",
                "Balanced fertilization — avoid excess nitrogen",
                "Compost tea spray to boost plant immunity",
            ],
            "chemical": [
                "Azoxystrobin + Propiconazole (Quilt Xcel) — 1 L/ha",
                "Pyraclostrobin (Headline EC) — apply at tasseling stage",
                "Mancozeb + Carbendazim (Saaf) — 2 g/L preventive",
                "Metconazole (Caramba) — systemic triazole fungicide",
            ],
        },
        "Corn_(maize)___healthy": {
            "display": "Corn — Healthy",
            "plant": "Corn (Maize)",
            "disease": None,
            "natural": [
                "Maintain regular irrigation schedule",
                "Apply balanced NPK fertilizer",
                "Monitor weekly for early pest/disease signs",
                "Keep fields weed-free to reduce competition",
            ],
            "chemical": [],
        },

        # ── Grape ─────────────────────────────────────────────────────────
        "Grape___Black_rot": {
            "display": "Grape — Black Rot",
            "plant": "Grapevine",
            "disease": "Black Rot (Guignardia bidwellii)",
            "natural": [
                "Remove and destroy all mummified berries and infected canes",
                "Prune to improve canopy air circulation",
                "Apply copper-based Bordeaux mixture (1%) before budbreak",
                "Use Neem oil spray (2%) every 7 days during wet periods",
                "Mulch soil to prevent spore splashing from ground",
            ],
            "chemical": [
                "Myclobutanil (Rally 40 WP) — apply from budbreak",
                "Mancozeb (Dithane M-45) — 2.5 g/L, 7-10 day intervals",
                "Captan (Captan 50 WP) — protective spray pre-bloom",
                "Tebuconazole (Folicur) — systemic, apply at bloom",
            ],
        },
        "Grape___Esca_(Black_Measles)": {
            "display": "Grape — Esca (Black Measles)",
            "plant": "Grapevine",
            "disease": "Esca / Black Measles (Phaeomoniella chlamydospora)",
            "natural": [
                "Remove and burn infected wood during winter pruning",
                "Paint pruning wounds with Trichoderma-based paste",
                "Avoid large pruning cuts — use double pruning technique",
                "Apply essential oil-based wound sealants",
                "Remove severely affected vines to prevent spread",
            ],
            "chemical": [
                "Fosetyl-Aluminium (Aliette 80 WG) — foliar spray",
                "Tebuconazole (Folicur 250 EW) — wound treatment",
                "Flusilazole (Punch 400 EC) — systemic fungicide",
                "Thiophanate-methyl (Topsin M) — trunk injection method",
            ],
        },
        "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
            "display": "Grape — Leaf Blight",
            "plant": "Grapevine",
            "disease": "Leaf Blight / Isariopsis Leaf Spot",
            "natural": [
                "Remove and destroy fallen infected leaves",
                "Improve vineyard ventilation by canopy management",
                "Spray Neem oil (2%) or garlic extract every 10 days",
                "Avoid wetting foliage during irrigation",
                "Apply compost to improve soil health and immunity",
            ],
            "chemical": [
                "Copper hydroxide (Kocide 2000) — 2 g/L preventive",
                "Mancozeb (Dithane M-45) — 2.5 g/L spray",
                "Azoxystrobin (Amistar 250 SC) — curative application",
                "Chlorothalonil (Daconil 720) — protective fungicide",
            ],
        },
        "Grape___healthy": {
            "display": "Grape — Healthy",
            "plant": "Grapevine",
            "disease": None,
            "natural": [
                "Perform regular canopy management and pruning",
                "Apply Bordeaux mixture preventively each season",
                "Monitor for insects and fungal signs weekly",
                "Ensure balanced potassium and calcium nutrition",
            ],
            "chemical": [],
        },

        # ── Tomato ────────────────────────────────────────────────────────
        "Tomato___Early_blight": {
            "display": "Tomato — Early Blight",
            "plant": "Tomato",
            "disease": "Early Blight (Alternaria solani)",
            "natural": [
                "Remove lower infected leaves immediately",
                "Spray baking soda solution (1 tsp/L water) weekly",
                "Apply compost tea to boost plant resistance",
                "Crop rotation — avoid tomatoes in same spot 3 years",
                "Mulch soil to prevent spore splash-up",
            ],
            "chemical": [
                "Chlorothalonil (Daconil 720 SC) — 2 ml/L every 7 days",
                "Mancozeb (Dithane M-45) — 2.5 g/L preventive spray",
                "Azoxystrobin (Amistar) — apply at first symptoms",
                "Copper oxychloride (Cuprosan) — 3 g/L protective",
            ],
        },
        "Tomato___Late_blight": {
            "display": "Tomato — Late Blight",
            "plant": "Tomato",
            "disease": "Late Blight (Phytophthora infestans)",
            "natural": [
                "Remove and destroy infected plants IMMEDIATELY",
                "Avoid overhead watering — use drip irrigation only",
                "Spray copper-based Bordeaux mixture (1%) preventively",
                "Ensure 60 cm+ spacing between plants for airflow",
                "Harvest green tomatoes if infection is severe",
            ],
            "chemical": [
                "Metalaxyl + Mancozeb (Ridomil Gold MZ) — 2.5 g/L",
                "Cymoxanil + Mancozeb (Curzate M) — 2.5 g/L spray",
                "Dimethomorph (Acrobat MZ) — systemic, 2 g/L",
                "Chlorothalonil (Daconil 720) — 2 ml/L protective",
            ],
        },
        "Tomato___Leaf_Mold": {
            "display": "Tomato — Leaf Mold",
            "plant": "Tomato",
            "disease": "Leaf Mold (Passalora fulva)",
            "natural": [
                "Improve greenhouse/tunnel ventilation immediately",
                "Reduce humidity below 85% using proper spacing",
                "Remove and bag infected leaves (do not compost)",
                "Spray diluted milk solution (1:9 ratio) weekly",
                "Plant resistant tomato varieties (Cf gene)",
            ],
            "chemical": [
                "Chlorothalonil (Daconil 720) — 2 ml/L every 10 days",
                "Mancozeb (Dithane M-45) — 2 g/L preventive spray",
                "Azoxystrobin (Amistar 250 SC) — curative treatment",
                "Trifloxystrobin (Flint 50 WG) — 0.2 g/L application",
            ],
        },
        "Tomato___healthy": {
            "display": "Tomato — Healthy",
            "plant": "Tomato",
            "disease": None,
            "natural": [
                "Water consistently at soil level (drip preferred)",
                "Apply balanced fertilizer (NPK 10-10-10) monthly",
                "Stake plants for support and airflow",
                "Monitor weekly for early pest/disease signs",
            ],
            "chemical": [],
        },
    },

    # ======================================================================
    #  F R E N C H
    # ======================================================================
    "fr": {
        # ── Maïs ─────────────────────────────────────────────────────────
        "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
            "display": "Maïs — Cercosporiose (Tache grise)",
            "plant": "Maïs",
            "disease": "Cercosporiose / Tache grise foliaire",
            "natural": [
                "Pratiquer la rotation des cultures tous les 2 ans pour briser le cycle de la maladie",
                "Éliminer et détruire les débris végétaux infectés après la récolte",
                "Pulvériser de l'huile de Neem diluée (2 %) tous les 7 à 10 jours",
                "Assurer un espacement adéquat entre les plants pour la circulation de l'air",
                "Éviter l'irrigation par aspersion — utiliser l'irrigation goutte-à-goutte",
            ],
            "chemical": [
                "Azoxystrobine (Amistar 250 SC) — appliquer dès les premiers symptômes",
                "Propiconazole (Tilt 250 EC) — 0,5 ml/L tous les 14 jours",
                "Mancozèbe (Dithane M-45) — 2,5 g/L en pulvérisation préventive",
                "Pyraclostrobine (Cabrio Top) — application foliaire",
            ],
        },
        "Corn_(maize)___Common_rust_": {
            "display": "Maïs — Rouille commune",
            "plant": "Maïs",
            "disease": "Rouille commune (Puccinia sorghi)",
            "natural": [
                "Planter des variétés hybrides de maïs résistantes à la rouille",
                "Semer tôt pour éviter le pic de la saison de rouille",
                "Éliminer les repousses spontanées de maïs autour des champs",
                "Appliquer du silicate de potassium en pulvérisation pour renforcer les feuilles",
                "Rotation des cultures avec des plantes non-hôtes (soja, blé)",
            ],
            "chemical": [
                "Propiconazole (Tilt 250 EC) — appliquer dès le début de l'infection",
                "Azoxystrobine + Propiconazole (Quilt Xcel) — action systémique",
                "Trifloxystrobine (Flint 50 WG) — application préventive",
                "Tébuconazole (Folicur 250 EW) — 1 ml/L, 2 applications",
            ],
        },
        "Corn_(maize)___Northern_Leaf_Blight": {
            "display": "Maïs — Helminthosporiose (Brûlure du Nord)",
            "plant": "Maïs",
            "disease": "Helminthosporiose du Nord (Exserohilum turcicum)",
            "natural": [
                "Utiliser des variétés hybrides résistantes (résistance gène Ht)",
                "Labourer en profondeur pour enfouir les résidus de culture infectés",
                "Rotation des cultures (éviter maïs après maïs)",
                "Fertilisation équilibrée — éviter l'excès d'azote",
                "Pulvérisation de thé de compost pour renforcer l'immunité de la plante",
            ],
            "chemical": [
                "Azoxystrobine + Propiconazole (Quilt Xcel) — 1 L/ha",
                "Pyraclostrobine (Headline EC) — appliquer au stade de la floraison mâle",
                "Mancozèbe + Carbendazime (Saaf) — 2 g/L en préventif",
                "Metconazole (Caramba) — fongicide triazole systémique",
            ],
        },
        "Corn_(maize)___healthy": {
            "display": "Maïs — Sain",
            "plant": "Maïs",
            "disease": None,
            "natural": [
                "Maintenir un programme d'irrigation régulier",
                "Appliquer un engrais NPK équilibré",
                "Surveiller chaque semaine les premiers signes de ravageurs ou maladies",
                "Garder les champs sans mauvaises herbes pour réduire la concurrence",
            ],
            "chemical": [],
        },

        # ── Vigne ─────────────────────────────────────────────────────────
        "Grape___Black_rot": {
            "display": "Vigne — Pourriture noire",
            "plant": "Vigne",
            "disease": "Pourriture noire (Guignardia bidwellii)",
            "natural": [
                "Éliminer et détruire toutes les baies momifiées et les sarments infectés",
                "Tailler pour améliorer la circulation de l'air dans la canopée",
                "Appliquer la bouillie bordelaise à base de cuivre (1 %) avant le débourrement",
                "Pulvériser de l'huile de Neem (2 %) tous les 7 jours en période humide",
                "Pailler le sol pour empêcher les éclaboussures de spores depuis le sol",
            ],
            "chemical": [
                "Myclobutanil (Rally 40 WP) — appliquer dès le débourrement",
                "Mancozèbe (Dithane M-45) — 2,5 g/L, intervalles de 7 à 10 jours",
                "Captane (Captan 50 WP) — pulvérisation protectrice avant floraison",
                "Tébuconazole (Folicur) — systémique, appliquer à la floraison",
            ],
        },
        "Grape___Esca_(Black_Measles)": {
            "display": "Vigne — Esca (Rougeole noire)",
            "plant": "Vigne",
            "disease": "Esca / Rougeole noire (Phaeomoniella chlamydospora)",
            "natural": [
                "Éliminer et brûler le bois infecté lors de la taille hivernale",
                "Appliquer une pâte à base de Trichoderma sur les plaies de taille",
                "Éviter les grosses coupes de taille — utiliser la technique de double taille",
                "Appliquer des mastics cicatrisants à base d'huiles essentielles",
                "Arracher les ceps gravement atteints pour empêcher la propagation",
            ],
            "chemical": [
                "Fosétyl-aluminium (Aliette 80 WG) — pulvérisation foliaire",
                "Tébuconazole (Folicur 250 EW) — traitement des plaies",
                "Flusilazole (Punch 400 EC) — fongicide systémique",
                "Thiophanate-méthyl (Topsin M) — injection dans le tronc",
            ],
        },
        "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
            "display": "Vigne — Brûlure foliaire",
            "plant": "Vigne",
            "disease": "Brûlure foliaire / Tache foliaire à Isariopsis",
            "natural": [
                "Ramasser et détruire les feuilles infectées tombées au sol",
                "Améliorer la ventilation du vignoble par la gestion de la canopée",
                "Pulvériser de l'huile de Neem (2 %) ou de l'extrait d'ail tous les 10 jours",
                "Éviter de mouiller le feuillage pendant l'irrigation",
                "Apporter du compost pour améliorer la santé du sol et l'immunité des plantes",
            ],
            "chemical": [
                "Hydroxyde de cuivre (Kocide 2000) — 2 g/L en préventif",
                "Mancozèbe (Dithane M-45) — 2,5 g/L en pulvérisation",
                "Azoxystrobine (Amistar 250 SC) — application curative",
                "Chlorothalonil (Daconil 720) — fongicide protecteur",
            ],
        },
        "Grape___healthy": {
            "display": "Vigne — Saine",
            "plant": "Vigne",
            "disease": None,
            "natural": [
                "Effectuer une gestion régulière de la canopée et de la taille",
                "Appliquer la bouillie bordelaise en préventif chaque saison",
                "Surveiller chaque semaine les insectes et les signes fongiques",
                "Assurer une nutrition équilibrée en potassium et en calcium",
            ],
            "chemical": [],
        },

        # ── Tomate ────────────────────────────────────────────────────────
        "Tomato___Early_blight": {
            "display": "Tomate — Alternariose",
            "plant": "Tomate",
            "disease": "Alternariose (Alternaria solani)",
            "natural": [
                "Supprimer immédiatement les feuilles basses infectées",
                "Pulvériser une solution de bicarbonate de soude (1 c. à café/L d'eau) chaque semaine",
                "Appliquer du thé de compost pour renforcer la résistance de la plante",
                "Rotation des cultures — éviter les tomates au même endroit pendant 3 ans",
                "Pailler le sol pour empêcher les éclaboussures de spores",
            ],
            "chemical": [
                "Chlorothalonil (Daconil 720 SC) — 2 ml/L tous les 7 jours",
                "Mancozèbe (Dithane M-45) — 2,5 g/L en pulvérisation préventive",
                "Azoxystrobine (Amistar) — appliquer dès les premiers symptômes",
                "Oxychlorure de cuivre (Cuprosan) — 3 g/L en protecteur",
            ],
        },
        "Tomato___Late_blight": {
            "display": "Tomate — Mildiou",
            "plant": "Tomate",
            "disease": "Mildiou (Phytophthora infestans)",
            "natural": [
                "Éliminer et détruire les plantes infectées IMMÉDIATEMENT",
                "Éviter l'arrosage par aspersion — utiliser uniquement l'irrigation goutte-à-goutte",
                "Pulvériser la bouillie bordelaise à base de cuivre (1 %) en préventif",
                "Assurer un espacement de 60 cm minimum entre les plants pour l'aération",
                "Récolter les tomates vertes si l'infection est sévère",
            ],
            "chemical": [
                "Métalaxyl + Mancozèbe (Ridomil Gold MZ) — 2,5 g/L",
                "Cymoxanil + Mancozèbe (Curzate M) — 2,5 g/L en pulvérisation",
                "Diméthomorphe (Acrobat MZ) — systémique, 2 g/L",
                "Chlorothalonil (Daconil 720) — 2 ml/L en protecteur",
            ],
        },
        "Tomato___Leaf_Mold": {
            "display": "Tomate — Cladosporiose",
            "plant": "Tomate",
            "disease": "Cladosporiose (Passalora fulva)",
            "natural": [
                "Améliorer immédiatement la ventilation de la serre ou du tunnel",
                "Réduire l'humidité en dessous de 85 % grâce à un espacement adéquat",
                "Retirer et mettre en sac les feuilles infectées (ne pas composter)",
                "Pulvériser une solution de lait dilué (ratio 1:9) chaque semaine",
                "Planter des variétés de tomates résistantes (gène Cf)",
            ],
            "chemical": [
                "Chlorothalonil (Daconil 720) — 2 ml/L tous les 10 jours",
                "Mancozèbe (Dithane M-45) — 2 g/L en pulvérisation préventive",
                "Azoxystrobine (Amistar 250 SC) — traitement curatif",
                "Trifloxystrobine (Flint 50 WG) — 0,2 g/L en application",
            ],
        },
        "Tomato___healthy": {
            "display": "Tomate — Saine",
            "plant": "Tomate",
            "disease": None,
            "natural": [
                "Arroser régulièrement au niveau du sol (goutte-à-goutte recommandé)",
                "Appliquer un engrais équilibré (NPK 10-10-10) chaque mois",
                "Tuteurer les plants pour le soutien et la circulation de l'air",
                "Surveiller chaque semaine les premiers signes de ravageurs ou maladies",
            ],
            "chemical": [],
        },
    },

    # ======================================================================
    #  A R A B I C
    # ======================================================================
    "ar": {
        # ── الذرة ─────────────────────────────────────────────────────────
        "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
            "display": "الذرة — تبقع السركسبورا (البقعة الرمادية)",
            "plant": "الذرة",
            "disease": "تبقع السركسبورا / البقعة الرمادية على الأوراق",
            "natural": [
                "تدوير المحاصيل كل سنتين لكسر دورة المرض",
                "إزالة وإتلاف بقايا النباتات المصابة بعد الحصاد",
                "رش زيت النيم المخفف (2%) كل 7 إلى 10 أيام",
                "ضمان تباعد مناسب بين النباتات لتهوية جيدة",
                "تجنب الري بالرش — استخدام الري بالتنقيط",
            ],
            "chemical": [
                "Azoxystrobin (Amistar 250 SC) — يُطبَّق عند ظهور الأعراض الأولى",
                "Propiconazole (Tilt 250 EC) — 0.5 مل/لتر كل 14 يومًا",
                "Mancozeb (Dithane M-45) — 2.5 غ/لتر رش وقائي",
                "Pyraclostrobin (Cabrio Top) — رش ورقي",
            ],
        },
        "Corn_(maize)___Common_rust_": {
            "display": "الذرة — الصدأ الشائع",
            "plant": "الذرة",
            "disease": "الصدأ الشائع (Puccinia sorghi)",
            "natural": [
                "زراعة أصناف ذرة هجينة مقاومة للصدأ",
                "الزراعة المبكرة لتجنب ذروة موسم الصدأ",
                "إزالة نباتات الذرة التطوعية حول الحقول",
                "رش سيليكات البوتاسيوم لتقوية الأوراق",
                "تدوير المحاصيل مع نباتات غير مضيفة (فول الصويا، القمح)",
            ],
            "chemical": [
                "Propiconazole (Tilt 250 EC) — يُطبَّق في بداية الإصابة",
                "Azoxystrobin + Propiconazole (Quilt Xcel) — مبيد جهازي",
                "Trifloxystrobin (Flint 50 WG) — تطبيق وقائي",
                "Tebuconazole (Folicur 250 EW) — 1 مل/لتر، تطبيقان",
            ],
        },
        "Corn_(maize)___Northern_Leaf_Blight": {
            "display": "الذرة — لفحة الأوراق الشمالية",
            "plant": "الذرة",
            "disease": "لفحة الأوراق الشمالية (Exserohilum turcicum)",
            "natural": [
                "استخدام أصناف هجينة مقاومة (مقاومة جين Ht)",
                "الحرث العميق لطمر بقايا المحاصيل المصابة",
                "تدوير المحاصيل (تجنب زراعة الذرة بعد الذرة)",
                "تسميد متوازن — تجنب الإفراط في النيتروجين",
                "رش شاي الكمبوست لتعزيز مناعة النبات",
            ],
            "chemical": [
                "Azoxystrobin + Propiconazole (Quilt Xcel) — 1 لتر/هكتار",
                "Pyraclostrobin (Headline EC) — يُطبَّق في مرحلة خروج الشرابة",
                "Mancozeb + Carbendazim (Saaf) — 2 غ/لتر وقائي",
                "Metconazole (Caramba) — مبيد فطري تريازولي جهازي",
            ],
        },
        "Corn_(maize)___healthy": {
            "display": "الذرة — سليمة",
            "plant": "الذرة",
            "disease": None,
            "natural": [
                "الحفاظ على جدول ري منتظم",
                "تطبيق سماد NPK متوازن",
                "المراقبة الأسبوعية للكشف المبكر عن الآفات والأمراض",
                "إبقاء الحقول خالية من الأعشاب الضارة لتقليل المنافسة",
            ],
            "chemical": [],
        },

        # ── العنب ─────────────────────────────────────────────────────────
        "Grape___Black_rot": {
            "display": "العنب — العفن الأسود",
            "plant": "الكرمة (العنب)",
            "disease": "العفن الأسود (Guignardia bidwellii)",
            "natural": [
                "إزالة وإتلاف جميع الحبات المحنطة والأغصان المصابة",
                "التقليم لتحسين دوران الهواء في المظلة الورقية",
                "تطبيق خليط بوردو النحاسي (1%) قبل تفتح البراعم",
                "رش زيت النيم (2%) كل 7 أيام خلال الفترات الرطبة",
                "تغطية التربة بالمهاد لمنع تناثر الأبواغ من الأرض",
            ],
            "chemical": [
                "Myclobutanil (Rally 40 WP) — يُطبَّق من بداية تفتح البراعم",
                "Mancozeb (Dithane M-45) — 2.5 غ/لتر، كل 7 إلى 10 أيام",
                "Captan (Captan 50 WP) — رش وقائي قبل الإزهار",
                "Tebuconazole (Folicur) — جهازي، يُطبَّق عند الإزهار",
            ],
        },
        "Grape___Esca_(Black_Measles)": {
            "display": "العنب — إسكا (الحصبة السوداء)",
            "plant": "الكرمة (العنب)",
            "disease": "إسكا / الحصبة السوداء (Phaeomoniella chlamydospora)",
            "natural": [
                "إزالة وحرق الخشب المصاب أثناء التقليم الشتوي",
                "طلاء جروح التقليم بمعجون يحتوي على فطر Trichoderma",
                "تجنب القطع الكبيرة أثناء التقليم — استخدام تقنية التقليم المزدوج",
                "تطبيق مواد سد الجروح المبنية على الزيوت العطرية",
                "اقتلاع الكروم المصابة بشدة لمنع انتشار المرض",
            ],
            "chemical": [
                "Fosetyl-Aluminium (Aliette 80 WG) — رش ورقي",
                "Tebuconazole (Folicur 250 EW) — معالجة الجروح",
                "Flusilazole (Punch 400 EC) — مبيد فطري جهازي",
                "Thiophanate-methyl (Topsin M) — طريقة الحقن في الجذع",
            ],
        },
        "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
            "display": "العنب — لفحة الأوراق",
            "plant": "الكرمة (العنب)",
            "disease": "لفحة الأوراق / تبقع الأوراق (Isariopsis)",
            "natural": [
                "إزالة وإتلاف الأوراق المصابة المتساقطة",
                "تحسين تهوية الكرم عبر إدارة المظلة الورقية",
                "رش زيت النيم (2%) أو مستخلص الثوم كل 10 أيام",
                "تجنب تبليل الأوراق أثناء الري",
                "إضافة الكمبوست لتحسين صحة التربة ومناعة النبات",
            ],
            "chemical": [
                "Copper hydroxide (Kocide 2000) — 2 غ/لتر وقائي",
                "Mancozeb (Dithane M-45) — 2.5 غ/لتر رش",
                "Azoxystrobin (Amistar 250 SC) — تطبيق علاجي",
                "Chlorothalonil (Daconil 720) — مبيد فطري وقائي",
            ],
        },
        "Grape___healthy": {
            "display": "العنب — سليمة",
            "plant": "الكرمة (العنب)",
            "disease": None,
            "natural": [
                "إجراء إدارة منتظمة للمظلة الورقية والتقليم",
                "تطبيق خليط بوردو وقائيًا كل موسم",
                "مراقبة الحشرات وعلامات الفطريات أسبوعيًا",
                "ضمان تغذية متوازنة بالبوتاسيوم والكالسيوم",
            ],
            "chemical": [],
        },

        # ── الطماطم ───────────────────────────────────────────────────────
        "Tomato___Early_blight": {
            "display": "الطماطم — اللفحة المبكرة",
            "plant": "الطماطم",
            "disease": "اللفحة المبكرة (Alternaria solani)",
            "natural": [
                "إزالة الأوراق السفلية المصابة فورًا",
                "رش محلول بيكربونات الصوديوم (1 ملعقة صغيرة/لتر ماء) أسبوعيًا",
                "تطبيق شاي الكمبوست لتعزيز مقاومة النبات",
                "تدوير المحاصيل — تجنب زراعة الطماطم في نفس المكان لمدة 3 سنوات",
                "تغطية التربة بالمهاد لمنع تناثر الأبواغ",
            ],
            "chemical": [
                "Chlorothalonil (Daconil 720 SC) — 2 مل/لتر كل 7 أيام",
                "Mancozeb (Dithane M-45) — 2.5 غ/لتر رش وقائي",
                "Azoxystrobin (Amistar) — يُطبَّق عند ظهور الأعراض الأولى",
                "Copper oxychloride (Cuprosan) — 3 غ/لتر وقائي",
            ],
        },
        "Tomato___Late_blight": {
            "display": "الطماطم — اللفحة المتأخرة (البياض الزغبي)",
            "plant": "الطماطم",
            "disease": "اللفحة المتأخرة (Phytophthora infestans)",
            "natural": [
                "إزالة وإتلاف النباتات المصابة فورًا",
                "تجنب الري بالرش — استخدام الري بالتنقيط فقط",
                "رش خليط بوردو النحاسي (1%) وقائيًا",
                "ضمان تباعد 60 سم على الأقل بين النباتات لتهوية جيدة",
                "قطف الطماطم الخضراء إذا كانت الإصابة شديدة",
            ],
            "chemical": [
                "Metalaxyl + Mancozeb (Ridomil Gold MZ) — 2.5 غ/لتر",
                "Cymoxanil + Mancozeb (Curzate M) — 2.5 غ/لتر رش",
                "Dimethomorph (Acrobat MZ) — جهازي، 2 غ/لتر",
                "Chlorothalonil (Daconil 720) — 2 مل/لتر وقائي",
            ],
        },
        "Tomato___Leaf_Mold": {
            "display": "الطماطم — العفن الورقي",
            "plant": "الطماطم",
            "disease": "العفن الورقي (Passalora fulva)",
            "natural": [
                "تحسين تهوية البيت البلاستيكي أو النفق فورًا",
                "تخفيض الرطوبة إلى أقل من 85% من خلال التباعد المناسب",
                "إزالة الأوراق المصابة ووضعها في أكياس (لا تُسمَّد)",
                "رش محلول الحليب المخفف (بنسبة 1:9) أسبوعيًا",
                "زراعة أصناف طماطم مقاومة (جين Cf)",
            ],
            "chemical": [
                "Chlorothalonil (Daconil 720) — 2 مل/لتر كل 10 أيام",
                "Mancozeb (Dithane M-45) — 2 غ/لتر رش وقائي",
                "Azoxystrobin (Amistar 250 SC) — علاج شفائي",
                "Trifloxystrobin (Flint 50 WG) — 0.2 غ/لتر تطبيق",
            ],
        },
        "Tomato___healthy": {
            "display": "الطماطم — سليمة",
            "plant": "الطماطم",
            "disease": None,
            "natural": [
                "الري بانتظام على مستوى التربة (يُفضَّل التنقيط)",
                "تطبيق سماد متوازن (NPK 10-10-10) شهريًا",
                "تعليق النباتات بالدعامات للتثبيت وتحسين التهوية",
                "المراقبة الأسبوعية للكشف المبكر عن الآفات والأمراض",
            ],
            "chemical": [],
        },
    },
}
