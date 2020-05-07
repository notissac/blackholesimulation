import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.style.use("ggplot")


#****************************************************************************#

def F_gravity(r, m, M):
    rr = np.sum(r*r)
    rhat = r/np.sqrt(rr)
    return (-G_gravity*m*M/rr)*rhat

def Fnet(r):
     
    F = np.zeros((N,N,2)) #stores the forces between all the bodies
    
    Fnet = np.zeros((N,2))
    
    for i in range(1,N-1):
        for j in range(i+1,N):
            F[i,0] = F_gravity(r[i] - r[0], mass[i], mass[0])
            F[i,j] = F_gravity(r[i] - r[j], mass[i], mass[j])
            F[j,i] = -F[i,j]
            
    F[8,0] = F_gravity(r[8] - r[0], mass[8], mass[0])
    
    for i in range(N):
        Fnet[i] = sum(F[i])
        
    return Fnet


    


#*****************************************************************************#

def dynamics(r0, v0, dt, t_max, iv = True):

    nsteps = int(t_max/dt)
    time = dt*np.arange(nsteps)
    r = np.zeros((nsteps, N, 2))
    v = np.zeros_like(r)
    r[0] = r0
    v[0] = v0
    
    Ft = Fnet(r0)
    
#****************************************************************************#
    #Velocity Verlets
    currenttime = 0
    for t in range(nsteps-1):
        
        if currenttime<1:
            mass[0] = 1
            currenttime = currenttime + dt
            
        else:
            mass[0] = blackholemass

        vhalf = v[t] + 0.5*dt*Ft/mass
        r[t+1] = r[t] + dt*vhalf
        Ftdt = Fnet(r[t+1])
        v[t+1] = vhalf + 0.5*dt*Ftdt/mass
        Ft = Ftdt
    
                       
    return t, r, v


#*******************************************************

if __name__ == "__main__":
    #------------------------------------------------------------
    # initialization
    #------------------------------------------------------------
    
    #Initialization
    
    N = 9
    
    mass = np.zeros((N,1))
    
    mass[1] = 1.660100e-6
    mass[2] = 2.447838e-6
    mass[3] = 3.003490e-6
    mass[4] = 3.227151e-7
    mass[5] = 9.547919e-4
    mass[6] = 2.858860e-4
    mass[7] = 4.366244e-5
    mass[8] = 5.151389e-5
    
    angle = np.array(([0, 160.470, 90.450, 70.510, 140.570, 33.420, 164.850, 205.640, 288.380]))
    
    period = np.array(([0, 0.24, 0.615, 1, 1.88, 11.86, 29.46, 84.0110, 164.7901]))
    
    distance = np.array(([0,0.39, 0.723, 1, 1.524, 5.203, 9.539, 19.18, 30.06]))
   
    
    #Initial Position
    
    r0 = np.zeros((N,2))

    for i in range(1,N):
        x = np.deg2rad(angle[i])
        r0[i] = distance[i] * np.array([np.cos(x), np.sin(x)])
    
    #Initial Velocity
    
 
    v0 = np.zeros((N,2))
    
    for i in range(1,N):
        x = np.deg2rad(angle[i])
        s = 2*np.pi*distance[i]/period[i]
        v0[i] = -s * np.array([-np.sin(x), np.cos(x)])
    
    
    #------------------------------------------------------------
    
    #***************PARAMETERS***********************
    
    
    G_gravity = 4*np.pi**2
    t_max = 2
    dt = 0.001
    
    mass[0] = 1
    
    #*********************************************
    #*******************************************
    #*******CHANGE THIS AND SEE THE TERROR**********
    
    blackholemass = 2000
    
    #*******************************************
    #**************************************
    #*********************************************
    #*****************************************
    #*********************************************
    #------------------------------------------------------------#
    
    #PLOTS
    
    
    time, r, v = dynamics(r0, v0, dt, t_max)
    
    #Assigning position vectors
    
    rC = r[:,0] #Center (Sun or Black Hole)
    rMe = r[:,1] #Mercury
    rV = r[:,2] #Venus
    rE = r[:,3] #Earth
    rMa = r[:,4] #Mars
    rJ = r[:,5] #Jupiter
    rS = r[:,6] #Saturn
    rU = r[:,7] #Uranus
    rN = r[:,8] #Neptune
    
    stop = np.zeros((N,1))
    
    for n in range(1,N):
        for x in r[:,n].tolist():
            if np.sqrt(x[0]**2+x[1]**2) < 0.5: #CHANGE WITH TIME STEP
                stop[n] = (r[:,n].tolist().index(x))
                break
    
    print("""This array shows the time step at which the planet 'n' approximately reaches the black hole.
            This information is used for the plots.
          The Sun and Mercury are not included.""") 
    print(stop[2:])
    
    
    #PLOT CODE 
    
    
    fig, ax = plt.subplots(figsize=(10,10))
    ax.plot(rC[:,0], rC[:, 1],'C1',label="Center")
    #ax.plot(rMe[:,0], rMe[:, 1],'C2', label="Mercury")
    ax.plot(rV[:,0][:1003], rV[:, 1][:1003],'C3', label="Venus")
    ax.plot(rE[:,0][:1004], rE[:, 1][:1004],'C4', label="Earth")
    ax.plot(rMa[:,0][:1008], rMa[:, 1][:1008],'C5', label="Mars")
    ax.plot(rJ[:,0][:1047], rJ[:, 1][:1047],'C6', label="Jupiter")
    ax.plot(rS[:,0][:1117], rS[:, 1][:1117],'C7', label="Saturn")
    ax.plot(rU[:,0][:1333], rU[:, 1][:1333],'C8', label="Uranus")
    ax.plot(rN[:,0][:1652], rN[:, 1][:1652],'C9', label="Neptune")
    
    
    ax.set_aspect(1)
    ax.set_xlabel(r"$x$ (AU)")
    ax.set_ylabel(r"$y$ (AU)")
    ax.legend(loc="best")
    
    ax.set_title("Orbits")

    
    print("""The approximate time it takes (in hours) for each planet, starting from Venus, 
          to be eaten by the black hole is, respectively:""", (stop.tolist()[2][0]-1000)*9,",",
          (stop.tolist()[3][0]-1000)*9,",",(stop.tolist()[4][0]-1000)*9,",",(stop.tolist()[5][0]-1000)*9,",",
         (stop.tolist()[6][0]-1000)*9,",",(stop.tolist()[7][0]-1000)*9,", and",(stop.tolist()[8][0]-1000)*9,)
    