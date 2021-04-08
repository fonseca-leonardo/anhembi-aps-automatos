class CheckVariableDeclaration:
    def execute(self, declaration):
        try:
            [varName, varValueWithSemiColon] = declaration.split('=')
            varNameWithoutSpace = varName.strip()
            varValueWithoutSpace = varValueWithSemiColon.strip()
            varValue = list(varValueWithoutSpace)

            if(not self.__semiColon(varValue[-1])):
                raise Exception("Precisa ter ponto e vírgula no final.")
            else:
                del varValue[-1]

            if(not self.__checkIsVarName(varNameWithoutSpace)):
                raise Exception("Precisa ser Letras")

            if(not self.__checkIsVarValue(varValue)):
                raise Exception("Precisa ser Letra ou so numero")

            print("Aceito.")

        except Exception as e:
            print(e)

    def __checkEqualSign(self, char):
        print("Sinal de igual \n")

    def __checkIsVarName(self, charset):
        varNameCharSet = list(charset)

        isString = False

        if(not self.__checkCapitalLetter(varNameCharSet[0])):
            raise Exception('Precisa começar com letra maiúscula.')

        del varNameCharSet[0]

        for varNameChar in varNameCharSet:
            if(self.__checkLowerCaseLetter(varNameChar) or self.__checkNumber(varNameChar)):
                isString = True
            else:
                raise Exception('Sem caracteres especiais.')

        return isString

    def __checkIsVarValue(self, charset):
        isStringOrNumber = False

        if(not self.__checkNumber(charset[0])):

            if(self.__checkIsVarName(charset)):
                isStringOrNumber = True
                return isStringOrNumber
        else:
            dotOccurances = 0
            for char in charset:
                if(char == '.'):
                    dotOccurances += 1
                else:
                    if(self.__checkNumber(char)):
                        isStringOrNumber = True
                    else:
                        raise Exception(
                            'Não pode ter letra no meio do número.')

            if(dotOccurances > 1):
                isStringOrNumber = False
                return isStringOrNumber

        return isStringOrNumber

    def __checkCapitalLetter(self, char: str):
        return char.isupper()

    def __checkLowerCaseLetter(self, char: str):
        return char.islower()

    def __checkNumber(self, char):
        numbers = '0123456789'
        isNumber = False

        for number in list(numbers):
            if(number == char):
                isNumber = True
                break

        return isNumber

    def __semiColon(self, char):
        isSemiColon = False

        if(char == ';'):
            isSemiColon = True

        return isSemiColon
