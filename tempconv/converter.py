def convert(text):
            if text.text() != "":
                if text.objectName() == "c_box":
                    try:
                        return str((float(text.text()) * (9 / 5)) + 32)
                    except ValueError:
                        return "Number only!"
                elif text.objectName() == "f_box":
                    try:
                        return str((float(text.text()) - 32) * (5 / 9))
                    except ValueError:
                        return "Number only"
                else:
                    return "An error has occurred. Try again."
            else:
                return ""
