# IEEE-754-Decimal-32-floating-point-converter
This is the simulation project that our professor, Mr. Roger Luis Uy, gave to the group as one of the requirements for passing CSARCH2.

# Contributors
Jordan Chester Chong
Mark Daniel Gutierrez
Miguel Carlo Kua
Kaci Reena Santos
Kevin Bryan Tuco

## How to Use the Converter
Download the files (GUI.py and logic folder). Once the files are downloaded, please initialize the GUI.py file.

## The Interface
The interface is comprised of 3 fields in which the user can input. The 3 fields are named: number, power, and rounding method. The number field is where the user will type in the number. The user may type in any number with any amount of digits. The power field indicates the power that the base_10 exponent has. Last but not least, the rounding method lists down all the ways where the user can round their number. There are 4 types that are in the rounding method field, namely: "Truncate", "Round Up", "Round Down", "Round, Ties to Nearest Even", and "Round, Ties Away from Zero". Once the user types in the required fields, then the program will show the results once the user clicks on the "Submit" button. The requested answers will be shown in the white box below. The users will also have a chance to export the answers to a .txt file by clicking on the button "Export to Text".
![image](https://github.com/jordanchong911/IEEE-754-Decimal-32-floating-point-converter/assets/94843916/206fde42-5d5d-4d23-a5a5-385d98b20644)

## Instructions on How to Use the Application
For example, the user wants to know the conversion of the number "0.000001 x 10 ^ -383". The user will first type in the number "0.000001" to the "Number" field. The user also types in the power "-383" to the "power" field. If the user wants to have a certain rounding method done, then they can select the specific rounding method that they would like. This user would like to truncate, so the user clicks on the "Truncate" option in the "Rounding Methods" field. Once everything is done, the user will click on the "Submit" button. This will show the corresponding answers as pictured below:
![image](https://github.com/jordanchong911/IEEE-754-Decimal-32-floating-point-converter/assets/94843916/c6dd44c1-8000-45fc-a165-49e0fc301b14)
If the user will like to export this answer to a text file, then the user will click on the "Export to Text" button. Once the user clicks on the "Export to Text" button, a prompt will appear, stating that the file is saved in "dpd_results.txt". The following screenshots below shows the prompt and the text file exported
![image](https://github.com/jordanchong911/IEEE-754-Decimal-32-floating-point-converter/assets/94843916/09ce8266-ce45-4582-a37a-ae677f5e6285)
![image](https://github.com/jordanchong911/IEEE-754-Decimal-32-floating-point-converter/assets/94843916/378ab9ae-ae50-47b5-ac3e-abdcad7e79cd)

## Restrictions
The user should not be able to submit empty fields, nor will the user be able to export a text file. Doing so may cause a prompt to show like the following picture:
![image](https://github.com/jordanchong911/IEEE-754-Decimal-32-floating-point-converter/assets/94843916/7fcc867d-fc59-45a5-965e-aba51ceebb0c)
Please be guided that **ONLY FILLED OUT FIELDS WITH NUMBERS ARE ALLOWED, STRINGS WILL NOT BE ACCEPTED.** The following picture shows if the user types in characters instead of numbers:
![image](https://github.com/jordanchong911/IEEE-754-Decimal-32-floating-point-converter/assets/94843916/66d0b2e0-7992-4b42-a888-417711a8b9b1)
