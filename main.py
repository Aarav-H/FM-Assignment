import matplotlib.pyplot as plt
import numpy as np

#Corporate tax rate 
tax=0.3

#Defining a class which stores all relavent information of each firm 
class Company:
    def __init__(self,de_ratio,intercept,name,beta_levered=None):
        self.beta_levered=beta_levered
        self.de_ratio=de_ratio
        self.intercept=intercept
        self.beta_unlevered: float = None
        self.name=name
        
#Function to unlever financial leverage from beta
def unlevering(beta_levered,de_ratio,tax):
  return beta_levered/((1+de_ratio)*(1-tax)) 
 
#Function to relever the beta        
def relevering(beta_unlevered,de_ratio,tax):
    return beta_unlevered*(1+(de_ratio*(1-tax)))

#Funtion calculating cost of equity
def costofequity(rf,x,beta_relevered):
    return rf+beta_relevered*(x)

#Function to calculate WACC
def WACC_calc(cost_of_debt,tax,Wb,cost_of_equity,Ws):
    return (cost_of_debt*(1-tax)*Wb)+(cost_of_equity*Ws)


def plot_graph(companies):
    plt.figure()
    for company in companies:
        x = np.linspace(0, 10, 101)
        y = company.intercept + company.beta_levered * x
        plt.plot(x, y, label =company.name)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
    

if __name__ ==  "__main__":
#Defining Company attributes
    HPCL=Company(2.33,-0.0005,"HPCL")
    BPCL=Company(1.14,-0.0022,"BPCL",1.2529)
    MRPL=Company(1.69,0.0082,"MRPL",1.3580)
    IOCL=Company(1,0.0021,"IOCL",1.0324)
    CPCL=Company(0.66,0.0118,"CPCL",1.3004)
    
#Step 1:Unlevering the betas
    BPCL.beta_unlevered=unlevering(BPCL.beta_levered,BPCL.de_ratio,tax)
    MRPL.beta_unlevered=unlevering(MRPL.beta_levered,MRPL.de_ratio,tax)
    IOCL.beta_unlevered=unlevering(IOCL.beta_levered,IOCL.de_ratio,tax)
    CPCL.beta_unlevered=unlevering(CPCL.beta_levered,CPCL.de_ratio,tax)
    
#Step 2:Calculating the average of the unlevered betas
    betas_unlevered=[BPCL.beta_unlevered,MRPL.beta_unlevered,IOCL.beta_unlevered,CPCL.beta_unlevered]
    mean_beta_unlevered=sum(betas_unlevered)/len(betas_unlevered)
    
#Step 3:Relevering the mean unlevered beta with respect to HPCL
    HPCL_relevered=relevering(mean_beta_unlevered,HPCL.de_ratio,tax)
    HPCL.beta_levered=HPCL_relevered
    #print(HPCL_relevered)
    
#Step 4:Calcutaing cost of equity and debt
    cost_of_equity=costofequity(0.0714,0.0143,HPCL_relevered)
   #print(cost_of_equity)
    cost_of_debt=0.14  #The interest coverage ratio of the firm was -4.52 which equated to a 14% interest rate on debt
   
#Step 5:Calculating the weightage of debt and equity 
    Ws=1/(1+HPCL.de_ratio)
    Wb=1-Ws
    
#Step 6:Calculating the WACC for the firm
    WACC=WACC_calc(cost_of_debt,tax,Wb,cost_of_equity,Ws)
    print("The value  of  WACC WACC", WACC)
    

    market_value_debt=64517.22
    market_value_equity=141.85*461.2
    
    plot_graph([BPCL, MRPL, IOCL, CPCL])