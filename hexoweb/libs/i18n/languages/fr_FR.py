"""
@Project   : fr_FR
@Author    : abudu & Deepseek
@Blog      : https://www.oplog.cn
"""

from ..core import Language


class Main(Language):
    name = 'fr_FR'
    name_local = "Français"
    default = {
        "name": name,
        "data": {
            "ADD": "Ajouter",
            "ADD_CATEGORY": "Ajouter une catégorie",
            "ADD_SUCCESS": "Ajouté avec succès !",
            "ADD_TAG": "Ajouter un tag",
            "ADVANCED": "Avancé",
            "ADVANCED_SETTINGS": "Paramètres avancés",
            "ADVANCED_SETTINGS_LABEL": "Paramètres avancés",
            "API_VERIFY_FAILED": "Échec de la vérification de l'API, IP d'accès: {}",
            "AUTHOR": "Auteur",
            "AUTO_PROVIDER_FAILED": "Erreur lors de la génération automatique du PROVIDER, veuillez vérifier la configuration et soumettre",
            "BACKUP": "Sauvegarde",
            "BOTTOM_PH": "Si plusieurs niveaux, veuillez utiliser le format JSON",
            "CACHE": "Cache",
            "CACHE_CLEAN_REQUEST": "Êtes-vous sûr de vouloir effacer tout le cache ?",
            "CANCEL": "Annuler",
            "CAPTCHA_FAILED": "Échec de la vérification anti-robot !",
            "CAPTCHA_GET_FAILED": "Échec de la récupération",
            "CAPTCHA_NO": "Aucune information de vérification anti-robot reçue",
            "CAPTCHA_RESULT": "Résultat de reCaptcha{}: {}",
            "CATEGORY_EXITS": "Catégorie existante !",
            "CHANGE_LANGUAGE": "Changer de langue",
            "CLEAN_FLINKS_FAILED": "Aucun lien amical caché",
            "CLEAN_FLINKS_SUCCESS": "{} liens amicaux ont été nettoyés avec succès",
            "CLEAR_ALL": "Tout effacer",
            "CLOSE": "Fermer",
            "CLOUD_SCRIPTS": "Bibliothèque de commandes cloud",
            "COMMAND": "Commande",
            "CONFIG": "Configuration",
            "CONFIGS_LIST": "Liste des configurations",
            "CONFIG_LABEL": "Toutes les configurations",
            "CONFIG_NAME": "Nom de la configuration",
            "CONFIRM": "Confirmer",
            "CONFIRM_CLEAN_FLINK": "Êtes-vous sûr de vouloir nettoyer les liens cachés ? Cette opération est irréversible",
            "CONFIRM_DEL_CUSTOM": "Êtes-vous sûr de vouloir supprimer le champ {0} ? Cette opération est irréversible",
            "CONFIRM_FIX": "Êtes-vous sûr de vouloir tenter une réparation automatique ? Cela vérifiera et créera/supprimera les champs appropriés",
            "CONFIRM_RUN": "Êtes-vous sûr de vouloir exécuter {0} ? Cette opération ne peut être interrompue",
            "CONSOLE": "Panneau de contrôle",
            "CONTENT": "Contenu",
            "CURRENT_ENV": "Environnement actuel",
            "CUSTOM": "Personnalisé",
            "CUSTOMIZE": "Personnaliser",
            "CUSTOMIZE_LABEL": "Options de style du tableau de bord",
            "CUSTOM_LABEL": "Champ personnalisé",
            "CUSTOM_LIST": "Champs personnalisés",
            "DARKMODE": "Clair / Sombre",
            "DASHBOARD": "Tableau de bord",
            "DELETING": "Suppression en cours...",
            "DEL_CONFIRM_1": "Êtes-vous sûr de vouloir supprimer",
            "DEL_CONFIRM_2": "? Cette opération est irréversible",
            "DEL_FAILED": "Échec de la suppression",
            "DEL_POST_INDEX": "Supprimer l'index des détails de l'article",
            "DEL_REMOTE": "Supprimer le fichier distant",
            "DEL_SUCCESS": "Supprimé avec succès !",
            "DEL_SUCCESS_AND_DEPLOY": "Supprimé avec succès et déploiement soumis !",
            "DEL_TMP": "Supprimer le répertoire temporaire",
            "DEL_VALUE": "Supprimer le champ",
            "DESCRIPTION": "Description",
            "DOC": "Documentation",
            "DRAFT": "Brouillon",
            "DRAFT_SAVE_SUCCESS": "Brouillon enregistré avec succès !",
            "DRAFT_SAVE_SUCCESS_AND_DEPLOY": "Brouillon enregistré avec succès et déploiement soumis !",
            "EDIT": "Éditer",
            "EDIT_CONFIG": "Éditer la configuration",
            "EDIT_FLINK": "Éditer le lien amical",
            "EDIT_PAGE": "Éditer la page",
            "EDIT_PAGE_LABEL": "Éditer la page",
            "EDIT_POST": "Éditer l'article",
            "EDIT_POST_LABEL": "Éditer l'article",
            "EDIT_SIDEBAR": "Éditer la barre latérale",
            "EDIT_SUCCESS": "Modifié avec succès !",
            "EDIT_TALK": "Éditer le talk",
            "EDIT_TALK_LABEL": "Éditer le talk",
            "EDIT_TALK_PH": "Écrivez votre talk ici...",
            "ELEVATOR_ERROR": "Erreur lors de la migration automatique de la mise à jour : {}",
            "ELEVATOR_START": "Démarrage de la migration automatique de la mise à jour... depuis {}",
            "ERROR": "Erreur",
            "ERROR_GETTING_PROVIDER": "Erreur lors de la récupération du PROVIDER",
            "EXCERPT_FAILED": "Échec de la récupération du résumé : ",
            "EXCERPT_LOADING": "Chargement du résumé...",
            "EXCERPT_LOCAL_LENGTH": "Longueur du résumé",
            "EXCERPT_LOCAL_LENGTH_PH": "Longueur à extraire",
            "EXCERPT_TIANLI_KEY": "Clé utilisateur",
            "EXCERPT_TIANLI_KEY_PH": "Clé utilisateur obtenue sur Aifadian",
            "EXCERPT_TIANLI_LENGTH": "Longueur envoyée",
            "EXCERPT_TIANLI_LENGTH_PH": "Longueur du contenu envoyé au serveur",
            "EXPORT": "Exporter",
            "FIND_INDEX_FAILED": "Échec de la mise à jour : répertoire Index non trouvé",
            "FIND_INDEX_SUCCESS": "Répertoire Index trouvé",
            "FIND_UPDATE_INDEX": "Décompression terminée, recherche du répertoire Index",
            "FINISH": "Terminé",
            "FIXING": "Réparation en cours... Veuillez patienter",
            "FIX_DISPLAY": "{} champs ont été réparés automatiquement, veuillez vérifier et modifier la configuration ultérieurement",
            "FIX_SUCCESS": "{} paramètres réparés",
            "FIX_VALUE": "Corriger le champ",
            "FLINK": "Lien amical",
            "FLINKS_LIST": "Liens amicaux",
            "FLINK_LABEL": "Liens amicaux",
            "FORCE_MSG": "Êtes-vous sûr de vouloir forcer la soumission ?",
            "FORCE_SUBMIT": "Soumettre de force",
            "FRONT_MATTER_GET_ERROR": "Erreur de parsing de FrontMatter : {}",
            "GET_ADVANCED_SETTINGS_FAILED": "Erreur lors de la récupération des paramètres avancés : {}",
            "GET_CUSTOM_FAILED": "Erreur lors de la récupération des champs personnalisés : {}",
            "GET_PAGE_SCAFFOLD_FAILED": "Échec de la récupération du modèle de page, message d'erreur : {}",
            "GET_POST_SCAFFOLD_FAILED": "Échec de la récupération du modèle d'article, message d'erreur : {}",
            "GET_SCRIPTS_FAILED": "Erreur lors de la récupération de la bibliothèque de fonctions en ligne : {}",
            "GET_SETTINGS_FAILED": "Erreur lors de la récupération de la configuration, redirection vers la page de mise à jour de la configuration",
            "GET_UPDATE_FAILED": "Échec de la récupération de la mise à jour",
            "GET_UPDATE_SUCCESS": "Mise à jour récupérée avec succès",
            "HAS_MSG_TIP_1": "Vous avez",
            "HAS_MSG_TIP_2": "messages non lus",
            "HEADER": "En-tête",
            "HELP": "Aide",
            "HELP_LABEL": "Besoin d'aide ?",
            "HELP_TIP": "Cliquez ici pour trouver la documentation",
            "HEXO_CONFIG": "\nConfiguration Hexo détectée",
            "HEXO_CONFIG_FAILED": "\nConfiguration Hexo non détectée",
            "HEXO_CONFIG_UPDATE": "\nMise à jour de la configuration Hexo réussie",
            "HEXO_CONFIG_UPDATE_FAILED": "\nÉchec de la validation de la configuration",
            "HEXO_INDEX_FAILED": "\nindex.html détecté, ce n'est peut-être pas le bon dépôt",
            "HEXO_PACKAGE": "\npackage.json détecté",
            "HEXO_PACKAGE_FAILED": "\npackage.json non détecté",
            "HEXO_SOURCE": "\nRépertoire source détecté",
            "HEXO_SOURCE_FAILED": "\nRépertoire source non détecté",
            "HEXO_THEME": "\nRépertoire thème détecté",
            "HEXO_THEME_FAILED": "\nRépertoire thème non détecté",
            "HEXO_TOKEN_FAILED": "Erreur de connexion distante ! Veuillez vérifier le Token",
            "HEXO_VERSION": "Version Hexo détectée : {}",
            "HEXO_VERSION_FAILED": "Hexo non détecté",
            "HOME": "Accueil",
            "ICON": "Icône",
            "ID_CODE": "Code d'identification",
            "IMAGE": "Image",
            "IMAGES_LIST": "Liste des images",
            "IMAGE_DEL_SUCCESS": "Enregistrement local supprimé",
            "IMAGE_LABEL": "Toutes les images",
            "IMAGE_LINK": "Lien de l'image",
            "IMAGE_NAME": "Nom de l'image",
            "IMPORT": "Importer",
            "IMPORT_WARN": "Après l'importation, vous perdrez toutes les informations existantes, veuillez confirmer !",
            "INDEX_GITHUB_TIP": "Soutenez l'auteur",
            "INDEX_GUIDE_LABEL": "Que voulez-vous faire maintenant ?",
            "INDEX_GUIDE_LABEL_1": "Nouvel article",
            "INDEX_GUIDE_LABEL_2": "Nouvelle page",
            "INDEX_GUIDE_LABEL_3": "Nouveau lien amical",
            "INDEX_GUIDE_LABEL_4": "Nouveau talk",
            "INDEX_GUIDE_TIP_1_P1": "Écrivez votre",
            "INDEX_GUIDE_TIP_1_P2": "nouvelle idée",
            "INDEX_GUIDE_TIP_2_P1": "Créez votre",
            "INDEX_GUIDE_TIP_2_P2": "nouvelle page",
            "INDEX_GUIDE_TIP_3_P1": "Ajoutez votre",
            "INDEX_GUIDE_TIP_3_P2": "nouvel ami",
            "INDEX_GUIDE_TIP_4_P1": "Partagez votre",
            "INDEX_GUIDE_TIP_4_P2": "nouvelle actualité",
            "INDEX_IMAGE_LABEL": "Total des images",
            "INDEX_IMAGE_TIP": "Essayez la gestion des images",
            "INDEX_POST_LABEL": "Total des articles",
            "INDEX_POST_TIP": "Avez-vous écrit un article aujourd'hui ?",
            "INDEX_RANDOM_POSTS": "Articles aléatoires",
            "INDEX_RECENT_IMAGES": "Images récentes",
            "INDEX_RECENT_POSTS": "Articles récents",
            "INDEX_VERSION_HASNEW": "Mise à jour détectée",
            "INDEX_VERSION_LABEL": "Version actuelle",
            "INDEX_VERSION_TIP": "Est à jour",
            "INIT": "Initialisation",
            "INIT_2_1": "Clé API",
            "INIT_2_1_PH": "Laisser vide pour générer automatiquement",
            "INIT_2_2": "Nom d'utilisateur",
            "INIT_2_2_PH": "Définir le nom d'utilisateur",
            "INIT_2_3": "Mot de passe",
            "INIT_2_3_PH": "Définir le mot de passe",
            "INIT_2_4": "Confirmer le mot de passe",
            "INIT_2_4_PH": "Ré-entrer pour confirmer le mot de passe",
            "INIT_3_1": "Fournisseur",
            "INIT_3_2": "Utiliser la configuration",
            "INIT_4_1": "Clé Vercel",
            "INIT_4_2": "ID du projet",
            "INIT_BLOG": "Configuration du blog",
            "INIT_FINISH": "Félicitations, vous avez terminé l'initialisation",
            "INIT_IMAGE": "Configuration du service d'images",
            "INIT_LOGIN_MSG_1": "Veuillez noter vos informations de connexion :",
            "INIT_LOGIN_MSG_2": "Nom d'utilisateur : ",
            "INIT_LOGIN_MSG_3": "Mot de passe : votre valeur définie",
            "INIT_LOGIN_MSG_4": "Connectez-vous au panneau de contrôle",
            "INIT_PROVIDER_FAILED": "Erreur lors de l'initialisation du PROVIDER : {}",
            "INIT_SUCCESS": "Initialisation terminée, redirection vers la page d'accueil",
            "INIT_USER": "Configuration de l'utilisateur",
            "INIT_USER_FAILED": "Erreur lors de l'initialisation du nom d'utilisateur et du mot de passe : {}",
            "INIT_VERCEL": "Configuration de Vercel",
            "INIT_VERCEL_FAILED": "Erreur lors de l'initialisation de Vercel : {}",
            "INIT_WELCOME": "Bienvenue ! Veuillez sélectionner une langue pour commencer l'initialisation",
            "INPUT_ARGV": "Veuillez entrer les paramètres",
            "JUMPED": "Passé",
            "JUMP_UPDATE": "Mise à jour de la configuration détectée, redirection vers la page de mise à jour de la configuration",
            "JUMP_UPDATE_FAILED": "Échec de la détection de la mise à jour de la configuration, redirection vers la page de mise à jour",
            "LEAVE_CONFIRM": "Êtes-vous sûr de vouloir quitter ?",
            "LINK": "Lien",
            "LOADING": "Chargement en cours...",
            "LOCAL": "Local",
            "LOCAL_UPDATE_SUCCESS": "Mise à jour terminée, redémarrage du thread dans cinq secondes",
            "LOGIN": "Connexion",
            "LOGIN_FAILED": "Erreur d'information de connexion",
            "LOGIN_FAILED_1": "Le nom d'utilisateur ne peut pas être vide ! ",
            "LOGIN_FAILED_2": "Le mot de passe ne peut pas être vide ! ",
            "LOGIN_FAILED_3": "Veuillez compléter la vérification ! ",
            "LOGIN_SUCCESS": "Connexion réussie, en attente de redirection",
            "LOGOUT": "Déconnexion",
            "LOGOUT_SUCCESS": "Déconnexion réussie",
            "LOVE": "J'aime",
            "MEASURE_IMAGE": "images",
            "MEASURE_LINK": "liens",
            "MEASURE_POST": "articles",
            "MIGRATE": "Migrer",
            "MIGRATE_CONFIG_SUCCESS": "Migration de la configuration terminée !",
            "MIGRATE_CUSTOM_SUCCESS": "Migration des champs personnalisés terminée !",
            "MIGRATE_DB": "Début de la migration de la base de données",
            "MIGRATE_FAILED": "Échec de la migration de {} : {}",
            "MIGRATE_FLINKS_SUCCESS": "Migration des liens amicaux terminée !",
            "MIGRATE_IMAGE_SUCCESS": "Migration des images terminée !",
            "MIGRATE_LABEL": "Migrer la configuration",
            "MIGRATE_MSG_SUCCESS": "Migration des messages terminée !",
            "MIGRATE_POST_SUCCESS": "Migration de l'index des détails des articles terminée !",
            "MIGRATE_PV_SUCCESS": "Migration des PV terminée !",
            "MIGRATE_SUCCESS": "Migration terminée !",
            "MIGRATE_TALKS_SUCCESS": "Migration des talks terminée !",
            "MIGRATE_UV_SUCCESS": "Migration des UV terminée !",
            "MSG_LOADING": "Chargement des messages...",
            "MSG_LOAD_ERROR": "Échec du chargement des messages",
            "NAME": "Nom",
            "NAVBAR_FIX": "Fixer la barre de navigation",
            "NETWORK_ERROR": "Erreur réseau !",
            "NEW_FLINK": "Ajouter un lien amical",
            "NEW_NAME": "Nouveau nom",
            "NEW_PAGE": "Nouvelle page",
            "NEW_PAGE_LABEL": "Nouvelle page",
            "NEW_POST": "Nouvel article",
            "NEW_POST_LABEL": "Nouvel article",
            "NEW_VALUE": "Nouveau champ",
            "New": "Nouveau",
            "New - PH": "le fichier sera enregistré sous",
            "NEXT": "Suivant",
            "NEXT_PAGE": "Page suivante",
            "NOT_INIT": "Configuration d'initialisation non terminée, redirection vers la page d'initialisation",
            "NO_MSG_TIP": "Vous n'avez aucun message pour le moment ~",
            "NO_NEXT_PAGE": "Dernière page",
            "NO_OTHER_ARGV": "Aucun autre paramètre",
            "NO_PAGE_NAME": "Veuillez entrer un nom de page correct dans la barre supérieure !",
            "NO_PERMISSION": "L'utilisateur secondaire ne supporte pas cette opération !",
            "NO_POST_NAME": "Veuillez entrer un nom d'article correct dans la barre supérieure !",
            "NO_PREV_PAGE": "Première page",
            "ONEKEY_UPDATE": "Mise à jour en un clic",
            "OPERATION": "Opération",
            "OPERATION_SUCCESS": "Opération réussie !",
            "OTHER_ARGV": "Autres paramètres",
            "PAGE": "Page",
            "PAGES_LIST": "Liste des pages",
            "PAGE_403_LABEL": "Erreur ! Erreur 403",
            "PAGE_403_TIP": "Erreur de vérification - Veuillez vérifier si vous avez les permissions",
            "PAGE_404": "Page non trouvée : {}",
            "PAGE_404_LABEL": "Erreur ! Erreur 404",
            "PAGE_404_TIP": "Page introuvable - ",
            "PAGE_500": "Erreur du serveur : {}",
            "PAGE_500_LABEL": "Erreur ! Erreur 500",
            "PAGE_500_TIP": "Message d'erreur :",
            "PAGE_ARGV_LABEL": "Paramètres de la page",
            "PAGE_EXIST": "Page existante !",
            "PAGE_LABEL": "Toutes les pages",
            "PAGE_NAME": "Nom de la page",
            "PASSWORD": "Mot de passe",
            "POST": "Article",
            "POSTS_LIST": "Liste des articles",
            "POST_ARGV_LABEL": "Paramètres de l'article",
            "POST_EXIST": "Article existant !",
            "POST_LABEL": "Tous les articles",
            "POST_NAME": "Nom de l'article",
            "PREV_PAGE": "Page précédente",
            "PROJECT_PAGE": "Page du projet",
            "PROVIDER_NO_SUPPORT": "Fournisseur non supporté !",
            "PROVIDER_VERIFY_ERROR": "Erreur de vérification de la configuration",
            "PROVIDER_VERIFY_SUCCESS": "Résultat de la vérification du Provider : {}",
            "PUBLISHED": "Publié",
            "PUBLISH_SUCCESS": "Publication réussie !",
            "PURGE_ALL_CACHE_SUCCESS": "Cache tout effacé avec succès",
            "PURGE_CACHE": "Purger le cache",
            "QEXO_MSG": "Messages Qexo",
            "READ_FILE": "Lire le fichier",
            "REBUILD_CACHE_SUCCESS": "Cache {} reconstruit avec succès",
            "RENAME": "Renommer",
            "RENAME_SUCCESS": "Renommé avec succès !",
            "RENAME_SUCCESS_AND_DEPLOY": "Renommé avec succès et déploiement soumis !",
            "REQUIRED": "Obligatoire",
            "RESET": "Réinitialiser",
            "RESET_PASSWORD_NO": "Veuillez entrer un mot de passe correct !",
            "RESET_PASSWORD_NO_MATCH": "Les mots de passe ne correspondent pas !",
            "RESET_PASSWORD_NO_OLD": "Ancien mot de passe incorrect !",
            "RESET_PASSWORD_NO_PASSWORD": "Le mot de passe ne peut pas être vide !",
            "RESET_PASSWORD_NO_USERNAME": "Veuillez entrer un nom d'utilisateur correct !",
            "RESULT": "Résultat",
            "RETRY": "Réessayer",
            "RUNNING": "En cours d'exécution...",
            "SAVE_CUSTOM": "Enregistrer les champs personnalisés",
            "SAVE_FAILED": "Échec de l'enregistrement !",
            "SAVE_SETTING": "Enregistrer les paramètres",
            "SAVE_SUCCESS": "Enregistré avec succès !",
            "SAVE_SUCCESS_AND_DEPLOY": "Enregistré avec succès et déploiement soumis !",
            "SAVE_SUCCESS_REDIRECT": "Enregistré avec succès, redirection en cours...",
            "SAVING": "Enregistrement en cours...",
            "SCRIPTS_LABEL": "Commandes cloud",
            "SCRIPTS_LIST": "Bibliothèque de fonctions en ligne",
            "SCRIPT_ARGV_FAILED": "Veuillez entrer des paramètres corrects !",
            "SCRIPT_RUN": "Exécuter la commande cloud : {}",
            "SCRIPT_RUN_SUCCESS": "Exécution réussie",
            "SCRIPT_RUN_SUCCESS_LOG": "Exécution de {} réussie : {}",
            "SEARCH": "Rechercher",
            "SEARCH_CONFIG": "Rechercher la configuration",
            "SEARCH_CUSTOM": "Rechercher les champs",
            "SEARCH_FLINK": "Rechercher les liens amicaux",
            "SEARCH_IMAGE": "Rechercher les images",
            "SEARCH_ITEM": "Élément de recherche",
            "SEARCH_PAGE": "Rechercher les pages",
            "SEARCH_POST": "Rechercher les articles",
            "SEARCH_SCRIPT": "Rechercher les commandes",
            "SEARCH_SETTINGS": "Rechercher les paramètres",
            "SEARCH_TALK": "Rechercher les talks",
            "SETTINGS": "Paramètres",
            "SETTINGS_LABEL": "Modifier la configuration",
            "SET_ABBRLINK": "Configuration des liens abrégés",
            "SET_ABBRLINK_1": "Algorithme des liens abrégés",
            "SET_ABBRLINK_2": "Base des liens abrégés",
            "SET_API": "Configuration de l'API",
            "SET_API_1": "Clé API",
            "SET_API_1_PH": "Laisser vide pour rester inchangé",
            "SET_API_2": "Activer l'API de demande de liens amicaux",
            "SET_API_3": "Utiliser reCaptcha pour vérifier les demandes de liens amicaux",
            "SET_API_4": "Clé reCaptcha",
            "SET_API_4_PH": "Token du serveur reCaptchaV3",
            "SET_BLOG": "Configuration du blog",
            "SET_BLOG_1": "Fournisseur",
            "SET_BLOG_2": "Utiliser la configuration",
            "SET_CDN": "Configuration du CDN",
            "SET_CDN_1": "Fournisseur du CDN",
            "SET_CUSTOM": "Configuration personnalisée",
            "SET_CUSTOM_1": "Nom du site",
            "SET_CUSTOM_1_PH": "Par défaut Hexo Dashboard",
            "SET_CUSTOM_2": "Liaison du site",
            "SET_CUSTOM_2_PH": "Par défaut “ - ”",
            "SET_CUSTOM_3": "Logo du site",
            "SET_CUSTOM_3_PH": "Par défaut qexo.png dans images",
            "SET_CUSTOM_4": "ICÔNE du site",
            "SET_CUSTOM_4_PH": "Par défaut icon.png dans images",
            "SET_CUSTOM_5": "LOGO sombre",
            "SET_CUSTOM_5_PH": "Par défaut qexo-dark.png dans images",
            "SET_EXCERPT": "Configuration du résumé",
            "SET_EXCERPT_1": "Méthode d'extraction",
            "SET_EXCERPT_2": "Extraction automatique",
            "SET_EXCERPT_3": "Champ enregistré",
            "SET_EXCERPT_3_PH": "Généralement excerpt",
            "SET_IMAGE": "Configuration du service d'images",
            "SET_IMAGE_1": "Type de service d'images",
            "SET_NOTIFY": "Configuration des notifications",
            "SET_NOTIFY_1": "Fournisseur",
            "SET_SECURE": "Configuration de la sécurité",
            "SET_SECURE_1": "Clé utilisateur reCaptchaV3 pour la page de connexion",
            "SET_SECURE_1_PH": "Laisser vide pour désactiver la fonctionnalité",
            "SET_SECURE_2": "Clé serveur reCaptchaV3 pour la page de connexion",
            "SET_SECURE_2_PH": "Laisser vide pour désactiver la fonctionnalité",
            "SET_SECURE_3": "Clé utilisateur reCaptchaV2 pour la page de connexion",
            "SET_SECURE_3_PH": "Laisser vide pour désactiver la fonctionnalité",
            "SET_SECURE_4": "Clé serveur reCaptchaV2 pour la page de connexion",
            "SET_SECURE_4_PH": "Laisser vide pour désactiver la fonctionnalité",
            "SET_STATISTICS": "Configuration des statistiques",
            "SET_STATISTICS_1": "Activer l'API de statistiques",
            "SET_STATISTICS_2": "Domaines sécurisés pour les statistiques",
            "SET_STATISTICS_2_PH": "Entrez les mots-clés des domaines, séparés par des virgules",
            "SET_USER": "Configuration de l'utilisateur",
            "SET_USER_1": "Ancien mot de passe",
            "SET_USER_1_PH": "Veuillez entrer l'ancien mot de passe",
            "SET_USER_2": "Nouveau nom d'utilisateur",
            "SET_USER_2_PH": "Veuillez entrer le nouveau nom d'utilisateur",
            "SET_USER_3": "Nouveau mot de passe",
            "SET_USER_3_PH": "Veuillez entrer le nouveau mot de passe",
            "SET_USER_4": "Confirmer le mot de passe",
            "SET_USER_4_PH": "Ré-entrer pour confirmer le mot de passe",
            "SET_WEBHOOK": "Configurer WEBHOOK en un clic",
            "SIDEBAR_COLOR": "Couleur de la barre latérale",
            "SIDEBAR_EDIT_1": "Contenu avant les deux points",
            "SIDEBAR_EDIT_2": "Titre de la description",
            "SIDEBAR_EDIT_3": "Icône utilisée",
            "SIDEBAR_TYPE": "Type de barre latérale",
            "SIDEBAR_TYPE_LABEL": "Choisissez entre deux styles",
            "SIDEBAR_TYPE_TIP": "Vous ne pouvez modifier le style que sur le bureau",
            "SIZE": "Taille",
            "SKIP": "Passer",
            "START": "Démarrer",
            "START_COPY": "Suppression terminée, copie des fichiers en cours...",
            "START_DEL": "Début de la suppression des fichiers...",
            "START_EXTRACT_UPDATE": "Téléchargement de la mise à jour terminé, début de la décompression",
            "START_LOCAL_UPDATE": "Début de la mise à jour, utilisation de la solution locale, préparation du répertoire temporaire",
            "START_VERCEL_UPDATE": "Début de la mise à jour, utilisation de la solution Vercel",
            "STATUS": "Statut",
            "STILL_IMPORT": "Continuer",
            "SUBMIT": "Soumettre",
            "SUPPORT": "Support",
            "SYSTEM_ERROR": "Le système a rencontré une erreur !",
            "TAGS": "Tags",
            "TAG_EXITS": "Tag existant !",
            "TALK": "Talk",
            "TALKS_LIST": "Liste des talks",
            "TALK_ARGV_LABEL": "Paramètres du talk",
            "TALK_LABEL": "Tous les talks",
            "TEST": "Tester",
            "TEST_MESSAGE": "Si vous recevez ce message, cela signifie que votre configuration des messages est réussie",
            "THANK_LABEL": "Merci pour votre Star !",
            "TIME": "Temps",
            "TIPS": "Conseils",
            "UNKNOWN_SIDEBAR": "Barre latérale inconnue",
            "UNTITLED": "Sans titre",
            "UPDATE": "Mettre à jour",
            "UPDATED_AT": "Mis à jour à",
            "UPDATED_AT_PH": "Heure de mise à jour",
            "UPDATE_CHANNEL": "Canal de mise à jour",
            "UPDATE_CONFIG": "Mise à jour de la configuration",
            "UPDATE_CONTENT": "Mise à jour détectée : {}<br>{}<p>Allez sur <object><a href=\"/settings.html\">Paramètres</a></object> pour mettre à jour en ligne</p>",
            "UPDATE_LABEL": "Mise à jour du programme",
            "UPDATE_LIB": "Début de la mise à jour de la bibliothèque...",
            "UPDATE_NO_CHANNEL": "Aucun canal de mise à jour",
            "UPDATE_POST_INDEX": "Mise à jour de l'index des détails de l'article",
            "UPDATE_QUEUING": "Échec de la mise à jour : une déploiement est en cours",
            "UPDATE_SUCCESS": "Mise à jour réussie",
            "UPDATE_SUCCESS_DISPLAY": "Mise à jour réussie, veuillez patienter pendant le déploiement automatique !",
            "UPDATING": "Mise à jour en cours...",
            "UPLOAD": "Télécharger",
            "UPLOAD_FAILED": "Échec du téléchargement !",
            "UPLOAD_SUCCESS": "Téléchargement réussi !",
            "UPLOAD_TIP": "Télécharger une image",
            "USERNAME": "Nom d'utilisateur",
            "USER_IS_NOT_STAFF": "L'utilisateur secondaire {} a tenté d'accéder à {} sans autorisation",
            "USER_IS_NOT_STAFF_DEL": "L'utilisateur secondaire {} a tenté de supprimer {} sans autorisation",
            "USER_IS_NOT_STAFF_MODIFY": "L'utilisateur secondaire {} a tenté de modifier {} sans autorisation",
            "USER_IS_NOT_STAFF_RENAME": "L'utilisateur secondaire {} a tenté de renommer {} sans autorisation",
            "VALUE": "Champ",
            "VALUE_NAME": "Nom du champ",
            "VERIFY_FAILED": "Échec de la vérification",
            "WARN": "Avertissement",
            "WARN_RESET": "Êtes-vous sûr de vouloir réinitialiser la configuration personnalisée ? Cette opération est irréversible",
            "WARN_WEBHOOK": "Êtes-vous sûr de vouloir créer automatiquement un événement Webhook ? Cela supprimera tous les événements Webhook de votre dépôt d'origine",
            "WELCOME": "Bienvenue",
            "WIKI_LABEL": "Voir la documentation"
        }
    }
