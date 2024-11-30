

Earlier we learned about a single Push Button Switch. In this chapter, we will learn about Matrix Keyboards, which integrates a number of Push Button Switches as Keys for the purposes of Input.

Project 22.1 Matrix Keypad
****************************************************************

In this project, we will attempt to get every key code on the Matrix Keypad to work.

Component List
================================================================

+-------------------------------------------------+-------------------------------------------------+
|1. Raspberry Pi (with 40 GPIO) x1                |                                                 |     
|                                                 | 4x4 Matrix Keypad x1                            |       
|2. GPIO Extension Board & Ribbon Cable x1        |                                                 |       
|                                                 |  |Keypad|                                       |                                                            
|3. Breadboard x1                                 |                                                 |                                                                 
+-------------------------------------------------+                                                 |
| Jumper wire                                     |                                                 |
|                                                 |                                                 |
|  |jumper-wire|                                  |                                                 |
+-------------------------------------------------+                                                 |
| Resistor 10kΩ x4                                |                                                 |
|                                                 |                                                 |
|  |Resistor-10kΩ|                                |                                                 |
+-------------------------------------------------+-------------------------------------------------+

.. |jumper-wire| image:: ../_static/imgs/jumper-wire.png
    :width: 50%
.. |Resistor-10kΩ| image:: ../_static/imgs/Resistor-10kΩ.png
    :width: 15%
.. |Keypad| image:: ../_static/imgs/Keypad.png

Component knowledge
================================================================

4x4 Matrix Keypad
----------------------------------------------------------------

A Keypad Matrix is a device that integrates a number of keys in one package. As is shown below, a 4x4 Keypad Matrix integrates 16 keys (think of this as 16 Push Button Switches in one module):

.. image:: ../_static/imgs/Keypad_1.png
    :align: center

Similar to the integration of an LED Matrix, the 4x4 Keypad Matrix has each row of keys connected with one pin and this is the same for the columns. Such efficient connections reduce the number of processor ports required. The internal circuit of the Keypad Matrix is shown below.

.. image:: ../_static/imgs/Keypad_2.png
    :align: center

The method of usage is similar to the Matrix LED, by using a row or column scanning method to detect the state of each key's position by column and row. Take column scanning method as an example, send low level to the first 1 column (Pin1), detect level state of row 5, 6, 7, 8 to judge whether the key A, B, C, D are pressed. Then send low level to column 2, 3, 4 in turn to detect whether other keys are pressed. Therefore, you can get the state of all of the keys.

Circuit
================================================================

+------------------------------------------------------------------------------------------------+
|   Schematic diagram                                                                            |
|                                                                                                |
|   |Keypad_Sc|                                                                                  |
+------------------------------------------------------------------------------------------------+
|   Hardware connection. If you need any support,please feel free to contact us via:             |
|                                                                                                |
|   support@freenove.com                                                                         |
|                                                                                                |
|   |Keypad_Fr|                                                                                  | 
+------------------------------------------------------------------------------------------------+

.. |Keypad_Sc| image:: ../_static/imgs/Keypad_Sc.png
.. |Keypad_Fr| image:: ../_static/imgs/Keypad_Fr.png



