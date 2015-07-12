
# coding: utf-8

# In[2]:




# In[3]:


"""




# In[10]:

spend = 10000
CTR = 0.003
CPM = 1.5
CR = 0.03
target_CPO = 45
avg_warenkorb = 150


# In[31]:

def calculate_cpo():
    impressions = int((spend / CPM) * 1000)
    clicks = int(impressions * CTR)
    conversions = int(clicks * CR)
    revenue = conversions * avg_warenkorb
    real_CPO = round((spend / conversions), 2)
    
    if real_CPO > target_CPO:
        return "Not profitable. Given the data you provided, this offer will result in a CPO of %s euro, which lies above your target CPO of %s euro." % (real_CPO, target_CPO)
    
    else:
        return "Profitable. Given the data you provided, this offer will result in a CPO of %s euro, which lies within your target CPO of %s euro. Expected clicks: %s, expected conversions: %s." % (real_CPO, target_CPO, clicks, conversions)
    

"""
# In[2]:


def user_input():
    print "Welcome to the CPM Profitability Calculator. If you received a Display offer from a publisher and are not sure if the CPM they charge is low or high, \
    this calculator is for you. \
    Please answer the following questions to find out if the Display CPM quota you received will return profit, according to your KPIs."
    
    cpm = raw_input("What is the CPM (Cost per Million Impressions) you were offered? ")
    cr = raw_input("What is the average, overall conversion rate of your website? ")
    ctr = raw_input("What is the average, historical CTR of your Non-Retargeting Display campaigns? (if first time action, type '0.3') ")
    basket_val = raw_input("What is your average shopping cart value? ")
    
    target_kpi = raw_input("What is your target KPI? Options: CPO, CRR ").lower().strip()

    if target_kpi == "cpo":
        target_cpo = raw_input("What is your target CPO? ")
        target_crr = None
    elif target_kpi == "crr":
        target_crr = raw_input("What is your target CRR? ")
        target_cpo = None
    else:
        print "You didnt type in a valid target kpi"

    budget = raw_input("How much budget would you like to spend? ")

    all_kpis = [cpm, cr, ctr, basket_val, target_cpo, target_crr, budget]
    user_kpis = [x for x in all_kpis if x is True]

    for var in user_kpis:
        if "," in var:
            var = float(var.replace(",", "."))
        if "%" in var:
            var = float(var.replace("%", ""))
        if "€" in var:
            var = float(var.replace("€", ""))
    
    return user_kpis

def profit_calculation(cpm, cr, ctr, basket_val, target_cpo, budget):

    impressions = int((spend / CPM) * 1000)
    clicks = int(impressions * CTR)
    conversions = int(clicks * CR)
    revenue = conversions * avg_warenkorb
    real_CPO = round((spend / conversions), 2)



'''



from Tkinter import *
mGui = Tk()


def calculate_cpo():
    mCPM = CPM.get()
    mSpend = Spend.get()
    mCTR = CTR.get()
    mCR = CR.get()
    mTarget_CPO = Target_CPO.get()
    impressions = int((mSpend / mCPM) * 1000)
    clicks = int(impressions * mCTR)
    conversions = int(clicks * mCR)
    real_CPO = round((mSpend / conversions), 2)
    
    if real_CPO > target_CPO:
        message = "Not profitable. Given the data you provided, this offer will result in a CPO of %s euro, which lies above your target CPO of %s euro." % (real_CPO, mTarget_CPO)
    
    else:
        message = "Profitable. Given the data you provided, this offer will result in a CPO of %s euro, which lies within your target CPO of %s euro. Expected clicks: %s, expected conversions: %s." % (real_CPO, mTarget_CPO, clicks, conversions)

    mresult = Label(mGui, text=message).pack()
    print message


# Variables

CPM = StringVar()
Spend = DoubleVar()
CTR = DoubleVar()
CR = DoubleVar()
Target_CPO = DoubleVar()

# Visuals

mGui.geometry("400x400")
mGui.title("Profitability Calculator")
mlabel = Label(text="Is this CPM too expensive?")
mlabel.pack()

mlabel1 = Label(text="Enter the CPM price:").pack()
mEntryCPM = Entry(mGui, textvariable=CPM).pack()
mlabel2 = Label(text="Enter your budget:").pack()
mEntrySpend = Entry(mGui, textvariable=Spend).pack()
mlabel3 = Label(text="Enter your predicted CTR:").pack()
mEntryCTR = Entry(mGui, textvariable=CTR).pack()
mlabel4 = Label(text="Enter your predicted CR:").pack()
mEntryCR = Entry(mGui, textvariable=CR).pack()
mlabel5 = Label(text="Enter your target CPO:").pack()
mEntryTarget_CPO = Entry(mGui, textvariable=Target_CPO).pack()

def calculate_cpo():
    blah = mEntryCPM.get()
    lab = Label(mGui, text=blah).pack()


mbutton = Button(text="Calculate", command=calculate_cpo).pack()

mGui.mainloop()



'''