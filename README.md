## MicroACurrencyCon

### Request Data:
<p>To request data, an input needs to be written into <b>input.txt</b>.<br>This input must follow a specific format for the microservice to register it as an input.<br> As all currencies have been given acronym equivalents which are listed in [Currency_List](https://github.com/Wagical/MicroACurrencyCon/blob/main/Currency_List.txt)<br> </p>

#### Example call:
<p>f = open("input.txt", "w")<br>f.write(f"{Origin} {Destination} {Amount}")<br>f.close<br></p>

### Receive Data:
<p>To receive data, after having given input if the correct formatting was done and the values were within the accepting range.<br> It will have written the results over the input within the txt file.<br>Make sure to have at least a partial delay to make sure the results are written quickly enough before you pull the results.</p>

#### Example Call:
<p>f = open("input.txt", "r")<br>time.sleep(.6)<br>result = f.read()</p>

#### Diagram:
![image](https://github.com/user-attachments/assets/6ba8ac85-b0e3-465b-ba36-b3de14e8bef0)

