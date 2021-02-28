import numpy as np
import math

labels = np.array(['Day', 'Outlook', 'Temperature', 'Humidity', 'Wind', 'PlayTennis'])

tennisData = np.array([['D1', 'Sunny', 'Hot', 'High', 'Weak', 'No'],
                       ['D2', 'Sunny', 'Hot', 'High', 'Strong', 'No'],
                       ['D3', 'Overcast', 'Hot', 'High', 'Weak', 'Yes'],
                       ['D4', 'Rain', 'Mild', 'High', 'Weak', 'Yes'],
                       ['D5', 'Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
                       ['D6', 'Rain', 'Cool', 'Normal', 'Strong', 'No'],
                       ['D7', 'Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
                       ['D8', 'Sunny', 'Mild', 'High', 'Weak', 'No'],
                       ['D9', 'Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
                       ['D10', 'Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
                       ['D11', 'Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
                       ['D12', 'Overcast', 'Mild', 'High', 'Strong', 'Yes'],
                       ['D13', 'Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
                       ['D14', 'Rain', 'Mild', 'High', 'Strong', 'No']
                       ])


def predictit(features):
    daysIplay = []
    daysIdontplay = []
    Iplaytoday = 0
    Iaintplayintoday = 0
    sunnycount = 0
    overcastcount = 0
    raincount = 0
    hotdays = 0
    milddays = 0
    cooldays = 0
    highhumiddays = 0
    normalhumiddays = 0
    weakwinddays = 0
    strongwinddays = 0
    daysIplaygivensunny = 0
    daysIplaygivenovercast = 0
    daysIplaygivenrainy = 0
    daysIdontplaygivensunny = 0
    daysIdontplaygivenovercast = 0
    daysIdontplaygivenrainy = 0
    daysIplaygivenhot = 0
    daysIplaygivenmild = 0
    daysIplaygivencool = 0
    daysIdontplaygivenhot = 0
    daysIdontplaygivenmild = 0
    daysIdontplaygivencool = 0
    daysIplaygivenhighhumid = 0
    daysIplaygivennormalhumid = 0
    daysIdontplaygivenhighhumid = 0
    daysIdontplaygivennormalhumid = 0
    daysIplaygivenstrong = 0
    daysIdontplaygivenstrong = 0
    daysIplaygivenweak = 0
    daysIdontplaygivenweak = 0
    daysIplay = []
    daysIdontplay = []

    print('My prediction is based on this... "\n')

    labels = np.array(['Day', 'Outlook', 'Temperature', 'Humidity', 'Wind', 'PlayTennis'])

    tennisData = np.array([['D1', 'Sunny', 'Hot', 'High', 'Weak', 'No'],
                           ['D2', 'Sunny', 'Hot', 'High', 'Strong', 'No'],
                           ['D3', 'Overcast', 'Hot', 'High', 'Weak', 'Yes'],
                           ['D4', 'Rain', 'Mild', 'High', 'Weak', 'Yes'],
                           ['D5', 'Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
                           ['D6', 'Rain', 'Cool', 'Normal', 'Strong', 'No'],
                           ['D7', 'Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
                           ['D8', 'Sunny', 'Mild', 'High', 'Weak', 'No'],
                           ['D9', 'Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
                           ['D10', 'Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
                           ['D11', 'Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
                           ['D12', 'Overcast', 'Mild', 'High', 'Strong', 'Yes'],
                           ['D13', 'Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
                           ['D14', 'Rain', 'Mild', 'High', 'Strong', 'No']
                           ])
    print(labels)
    print(tennisData)
    print("\n")

    for i in range(len(tennisData)):
        if tennisData[i][5] == 'Yes':
            Iplaytoday += 1
            daysIplay.append(tennisData[i])
        else:
            Iaintplayintoday += 1
            daysIdontplay.append(tennisData[i])
    print(f"I play tennis {Iplaytoday} of 14 of the saturdays")
    print(f"I pass on tennis {Iaintplayintoday} of 14 of the saturdays \n")

    for i in range(len(tennisData)):
        if tennisData[i][1] == 'Sunny':
            sunnycount += 1
        elif tennisData[i][1] == 'Overcast':
            overcastcount += 1
        else:
            raincount += 1

        if tennisData[i][1] == 'Sunny' and tennisData[i][5] == 'Yes':
            daysIplaygivensunny += 1
        elif tennisData[i][1] == 'Sunny' and tennisData[i][5] == 'No':
            daysIdontplaygivensunny += 1
        elif tennisData[i][1] == 'Rain' and tennisData[i][5] == 'Yes':
            daysIplaygivenrainy += 1
        elif tennisData[i][1] == 'Rain' and tennisData[i][5] == 'No':
            daysIdontplaygivenrainy += 1
        elif tennisData[i][1] == 'Overcast' and tennisData[i][5] == 'Yes':
            daysIplaygivenovercast += 1
        elif tennisData[i][1] == 'Overcast' and tennisData[i][5] == 'No':
            daysIdontplaygivenovercast += 1

    for i in range(len(tennisData)):
        if tennisData[i][2] == 'Hot':
            hotdays += 1
        elif tennisData[i][2] == 'Mild':
            milddays += 1
        else:
            cooldays += 1

        if tennisData[i][2] == 'Hot' and tennisData[i][5] == 'Yes':
            daysIplaygivenhot += 1
        elif tennisData[i][2] == 'Hot' and tennisData[i][5] == 'No':
            daysIdontplaygivenhot += 1
        elif tennisData[i][2] == 'Mild' and tennisData[i][5] == 'Yes':
            daysIplaygivenmild += 1
        elif tennisData[i][2] == 'Mild' and tennisData[i][5] == 'No':
            daysIdontplaygivenmild += 1
        elif tennisData[i][2] == 'Cool' and tennisData[i][5] == 'Yes':
            daysIplaygivencool += 1
        elif tennisData[i][2] == 'Cool' and tennisData[i][5] == 'No':
            daysIdontplaygivencool += 1

    for i in range(len(tennisData)):
        if tennisData[i][3] == 'High':
            highhumiddays += 1
        else:
            normalhumiddays += 1

        if tennisData[i][3] == 'High' and tennisData[i][5] == 'Yes':
            daysIplaygivenhighhumid += 1
        elif tennisData[i][3] == 'High' and tennisData[i][5] == 'No':
            daysIdontplaygivenhighhumid += 1
        elif tennisData[i][3] == 'Normal' and tennisData[i][5] == 'Yes':
            daysIplaygivennormalhumid += 1
        elif tennisData[i][3] == 'Normal' and tennisData[i][5] == 'No':
            daysIdontplaygivennormalhumid += 1

    for i in range(len(tennisData)):
        if tennisData[i][4] == 'Strong':
            strongwinddays += 1
        else:
            weakwinddays += 1

        if tennisData[i][4] == 'Strong' and tennisData[i][5] == 'Yes':
            daysIplaygivenstrong += 1
        elif tennisData[i][4] == 'Strong' and tennisData[i][5] == 'No':
            daysIdontplaygivenstrong += 1
        elif tennisData[i][4] == 'Weak' and tennisData[i][5] == 'Yes':
            daysIplaygivenweak += 1
        elif tennisData[i][4] == 'Weak' and tennisData[i][5] == 'No':
            daysIdontplaygivenweak += 1

    probofyes = []
    probofno = []

    if features[0] == 'Sunny':
        probofyes.append(daysIplaygivensunny / Iplaytoday)
        probofno.append(daysIdontplaygivensunny / Iaintplayintoday)
    elif features[0] == 'Overcast':
        probofyes.append(daysIplaygivenovercast / Iplaytoday)
        probofno.append(daysIdontplaygivenovercast / Iaintplayintoday)
    else:
        probofyes.append(daysIplaygivenrainy / Iplaytoday)
        probofno.append(daysIdontplaygivenrainy / Iaintplayintoday)

    if features[1] == 'Hot':
        probofyes.append(daysIplaygivenhot / Iplaytoday)
        probofno.append(daysIdontplaygivenhot / Iaintplayintoday)
    elif features[1] == 'Mild':
        probofyes.append(daysIplaygivenmild / Iplaytoday)
        probofno.append(daysIdontplaygivenmild / Iaintplayintoday)
    else:
        probofyes.append(daysIplaygivencool / Iplaytoday)
        probofno.append(daysIdontplaygivencool / Iaintplayintoday)

    if features[2] == 'High':
        probofyes.append(daysIplaygivenhighhumid / Iplaytoday)
        probofno.append(daysIdontplaygivenhighhumid / Iaintplayintoday)
    else:
        probofyes.append(daysIplaygivennormalhumid / Iplaytoday)
        probofno.append(daysIdontplaygivennormalhumid / Iaintplayintoday)

    if features[3] == 'Strong':
        probofyes.append(daysIplaygivenstrong / Iplaytoday)
        probofno.append(daysIdontplaygivenstrong / Iaintplayintoday)
    else:
        probofyes.append(daysIplaygivenweak / Iplaytoday)
        probofno.append(daysIdontplaygivenweak / Iaintplayintoday)

    probofyes.append(Iplaytoday / len(tennisData))
    probofno.append(Iaintplayintoday / len(tennisData))

    PofYes = np.prod(probofyes)
    PofNo = np.prod(probofno)

    if probofyes > probofno:
        print("Probabilty says it's a Yes! You will play Tennis today")
    else:
        print("Probabilty says it's a No! You ain't playin' today , sucka!")

#This prediction returns a no on tennis for that day...
predictit(['Sunny', 'Cool', 'High', 'Strong'])


# 3 of five of these were right after I removed them from the
#data set and ran the algorithm on them so the accuracy is 3/5 or 60%
predictit(['Rain', 'Mild', 'Normal', 'Weak'])
predictit(['Sunny', 'Mild', 'Normal', 'Strong'])
predictit(['Overcast', 'Mild', 'High', 'Strong'])
predictit(['Overcast', 'Hot', 'Normal', 'Weak'])
predictit(['Rain', 'Mild', 'High', 'Strong'])

tester = [['D10', 'Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
          ['D11', 'Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
          ['D12', 'Overcast', 'Mild', 'High', 'Strong', 'Yes'],
          ['D13', 'Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
          ['D14', 'Rain', 'Mild', 'High', 'Strong', 'No']]
