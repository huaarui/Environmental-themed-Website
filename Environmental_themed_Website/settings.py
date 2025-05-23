from pathlib import Path

# 在项目中构建路径，例如：BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent




# 安全警告：对生产环境中使用的密钥保密！
SECRET_KEY = "django-insecure-@foko0#3@vn+hokfskbmmz!2srtuxm-v#63ej8w9tksx2m6wyr"

# 安全警告：不要在生产环境中开启调试！
DEBUG = True

# 用于配置可以访问当前站点的域名，当DEBUG配置为False时，它是一个必填项，设置ALLOWED_HOSTS=['*']允许所有的域名访问
ALLOWED_HOSTS = []


# 应用程序定义
# 项目需要加载的App包路径列表
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "environmental_app",
    "widget_tweaks",
]

# 项目中需要加载的中间件列表配置
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# 项目的根URL配置
ROOT_URLCONF = "Environmental_themed_Website.urls"

# 项目的模板配置
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Environmental_themed_Website.wsgi.application"


# 数据库
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "environmental_app",
        "USER": "root",
        "PASSWORD": "mysql",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}


# 密码验证
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# 国际化
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# 静态文件（CSS、JavaScript、图片）
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR /'static',
]

# 默认的主键字段类型
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
