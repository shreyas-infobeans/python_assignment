from datetime import *
def ValidateCard(expDate):
    if expDate>datetime.now().date():
        return 'Valid'
    else:
        raise RuntimeError("Card has expired")
