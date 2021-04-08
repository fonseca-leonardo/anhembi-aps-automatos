class CheckVariableDeclaration:
    def execute(self, declaration):
        try:
            [varName, varValue] = declaration.split('=')
            varNameCharSet = list(varName)
            if(not self.__checkCapitalLetter(varNameCharSet[0])):
                raise Exception('PRECISA COMEÇAR COM LETRA MAIÚSCULA.')

            for varNameChar in range(1,varNameCharSet):
                if(self.__checkLowerCaseLetter(varNameChar) or self.__checkNumber(varNameChar)):
                    print("A")



        except Exception as e:
            print(e)

    def __checkEqualSign(self, char):
        print("Sinal de igual \n")

    def __checkCapitalLetter(self, char):
       capitalLetters = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'
       isCapitalLetter = False

       for letter in list(capitalLetters):
           if(char == letter):
               isCapitalLetter = True
               break
        
       return isCapitalLetter


    def __checkLowerCaseLetter(self, char):
        lowerCaseLetters = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'.lower()
        isLowerCaseLetter = False

        for letter in list(capitalLetters):
            if(char == letter):
                isLowerCaseLetter = True
                break
        
        return isLowerCaseLetter

    def __checkNumber(self, char):
        numbers = '0123456789'
        isNumber = False

        for number in list(numbers):
            if(number == char):
                isNumber = True
                break
        
        return isNumber


    def __semiColumn(self, char):
        print("Ponto e vírgula \n")
