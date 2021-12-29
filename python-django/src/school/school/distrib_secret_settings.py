
# Don't edit this file distrib_secret_setting.py. Use only for distribution
# Copy this file to secret_setting.py and there set values
# Don't distrib secret_setting.py file. Use only in dev or production

def get_settings( ):
        
    settings = {        
        'SECRET_KEY' : '',
        'DATABASE_NAME' : '',
        'DATABASE_PASS' : '',
    }

    return settings

