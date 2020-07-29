#Detecting figures

class Figure:


    def __init__(self,outcome):
        self.outcome = outcome

    def sorting(self):
        return self.outcome.sort()

    @staticmethod
    def checking(outcome):

        figures = []
        is_full = []
        outcome.sort()

        if (1 in outcome) and (2 in outcome) and (3 in outcome) and (4 in outcome) and (5 in outcome):
            figures.append('straight')

        elif (2 in outcome) and (3 in outcome) and (4 in outcome) and (5 in outcome) and (6 in outcome):
            figures.append('bigger_straight')

        elif not figures:
            for die in outcome:
                counts = outcome.count(die)
                if counts == 2 and 'pair' + str(die) not in figures:
                    figures.append('pair' + str(die))
                    is_full.append('pair')

                elif counts == 3  and 'three' + str(die) not in figures:
                    figures.append('three' + str(die))
                    is_full.append('three')

                elif counts == 4  and ('four' + str(die)) not in figures:
                    figures.append('four' + str(die))

                elif counts == 5  and ('flush' + str(die)) not in figures:
                    figures.append('flush' + str(die))



        if 'pair' in is_full and 'three' in is_full:
            figures.clear()
            figures.append('full house')


        if figures == []:
            figures.append('empty hand')


        print(figures)
        return figures
