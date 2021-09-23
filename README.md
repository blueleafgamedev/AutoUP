# AutoUP
This is a terminal program that I use to run monthly updates and maintenance on Fedora. I also added a section for Ubuntu to show how easy it is to customize the program to suit the needs of your OS. In order to run it when you open your terminal, you must add the python command followed by the file path to the end of your ~/.bashrc file.

For exapmle, I run it with the following command, in my ~/.bashrc file, on my computer python /home/travis/Projects/Python/AutoUP/updates.py or python ~/Projects/Python/AutoUP/updates.py. To add this to my ~/.bashrc file, I write the following:
>echo "python /home/travis/Projects/Python/AutoUP/updates.py" >> ~/.bashrc

OR

>echo "python ~/Projects/Python/AutoUP/updates.py" >> ~/.bashrc

**NOTE**
If the emoji module is not currently installed on your system, they won't show up in the program. Install it with the following in your terminal:
>pip install emoji
