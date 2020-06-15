# Gamehelper_android
a simple game script using python + opencv

This game required you to press certain amount of time to build a bridge just fit the gap between you and target,the longer you press the longer the bridge will be. The building speed is fixed, whereas target distance changes every step.
 
 
  
### How does it work
it capture a screenshot and pull back to the computer, use matchTemplate in opencv to find target position, determine the distance between origin and target, and calculate the time required for pressing, then push the adb command to the phone.
 
  

### Running showcase
![image](https://raw.githubusercontent.com/definitelynotkk/Gamehelper_android/master/run.gif)
     
     
     
      
Target Detection (In red rectangle)
![image](https://raw.githubusercontent.com/definitelynotkk/Gamehelper_android/master/detection.png)
