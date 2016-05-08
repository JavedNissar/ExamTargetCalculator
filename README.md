
How To Use
=========
To start using this program, you first have to create a JSON file of the form <course name>.json where <course name> is the name of the course that you are creating a profile for. The profile must be arranged in the following way,
```JSON
{
	"term_marks":[100,77.5,62.5],
	"term_weights":[0.1,0.3,0.2],
	"exam_weight":0.4
	"course_target":81
}
```
Please note that term_marks and term_weights must be of the same length. Also, please note that the equation sum(term_weights)+exam_weight=1 must hold true, otherwise the results of the calculator will be strange. Then, type the following command and follow the instructions produced.
```Shell
python target_calculator.py
```
