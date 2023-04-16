# Brownian-Motion-Plotter

This project plots two graphs  
1. Simple Brownian Motion  
2. Geometric Brownian Motion  

by taking necessary parameters as inputs.

## Simple Brownian Motion

The Wiener process, also known as Brownian motion, is a mathematical model that describes the random movement of particles in a fluid, gas or other medium. It was first introduced by the mathematician Norbert Wiener in 1923.

The Wiener process is a continuous-time stochastic process with stationary and independent increments, and is characterized by a number of properties, including Gaussian distribution, zero mean, and continuous paths.

![image](https://user-images.githubusercontent.com/88557062/232315231-bec62091-ae18-4975-822f-330a41a18a2d.png)

Inputs taken from user are-
- Ending time
- No. of paths

## Geometric Brownian Motion

A geometric Brownian motion (GBM) (also known as exponential Brownian motion) is a continuous-time stochastic process in which the logarithm of the randomly varying quantity follows a Brownian motion (also called a Wiener process) with drift. It is an important example of stochastic processes satisfying a stochastic differential equation (SDE).

![image](https://user-images.githubusercontent.com/88557062/232315255-da121005-dc31-4cd1-b628-8cf6bf9c5c78.png)

Inputs taken from user are-
- Ending time
- No. of paths
- Drift
- Volatility
- Initial Value

## The Project

The project can be viewed [here](https://bit.ly/ma323_brownian_motion)

Input the values and click on 'SUBMIT'

![image](https://user-images.githubusercontent.com/88557062/232316067-65fe6f6c-88d5-4440-a69e-dc7431211821.png)

It also outputs the theoretical and experimental means and variances.

![image](https://user-images.githubusercontent.com/88557062/232316120-77fc52d2-2a8d-4e44-9b65-591ac47faa8a.png)

## How to run on PC

  1. Open terminal in the home folder
  2. run 'python manage.py migrate'
  3. run 'python manage.py runserver'
  4. open the localhost address given in the terminal in any browser
  5. Now fill all the required fields in the form and click submit
  
## Applications

Geometric Brownian motion is commonly utilized in the [Black-Scholes model](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model) to simulate stock prices, making it the most prevalent model for stock price behavior. Some of the reasons for its usage are:
- expected returns are not reliant on the stock price value
- the GBM process is positively valued like real stock prices
- the paths of GBM display the same level of irregularity as actual stock prices
- it is relatively simple to perform calculations with GBM processes. 

Furthermore, GBM has been applied to monitor trading strategies in addition to modeling stock prices.

However, GBM is not entirely true to life, and it fails to reflect actual stock prices' volatility changes, and the path of GBM is continuous with no jumps caused by unexpected events or news. 
