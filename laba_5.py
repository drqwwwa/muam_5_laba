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
    def save_plot(self,time,signal,filename="signal.png"):
        plt.plot(time,signal)
        plt.savefig(filename)
        plt.close()
time=np.linspace(0,1,1000)
signal_freq=5
carrier_freq=50

generator=SignalGenerator(signal_freq)
signal=generator.generate(time)

modulator=Modulator(carrier_freq)
am_signal=modulator.am_modulate(signal,time)
fm_signal=modulator.fm_modulate(signal,time)

visualizer=Visualizer()
visualizer.plot_signal(time,signal,"Original Signal")
visualizer.plot_signal(time,am_signal,"AM Signal")
visualizer.plot_signal(time,fm_signal,"FM Signal")