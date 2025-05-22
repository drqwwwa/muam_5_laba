import numpy as np
import matplotlib.pyplot as plt

class SignalGenerator:
    def __init__(self,frequency,amplitude=1.0):
        self.frequency=frequency
        self.amplitude=amplitude

    def generate(self,time):
        return self.amplitude*np.sin(2*np.pi*self.frequency*time)
class Modulator:
    def __init__(self,carrier_frequency):
        self.carrier_frequency=carrier_frequency

    def am_modulate(self,signal,time):
        carrier=np.sin(2*np.pi*self.carrier_frequency*time)
        return (1+signal)*carrier
    def fm_modulate(self,signal,time,modulation_index=1.0):
        phase=2*np.pi*self.carrier_frequency*time+modulation_index*signal
        return np.sin(phase)
class Visualizer:
    def plot_signal(self,time,signal,title="Signal"):
        plt.figure()
        plt.plot(time,signal)
        plt.title(title)
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.grid()
        plt.show()

    def add_noise(self,signal,noise_level=0.1):
        noise=np.random.normal(0,noise_level,len(signal))
        return signal+noise
