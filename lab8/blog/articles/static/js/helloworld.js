var groupmates = [
    {
        "name": "Арина",
        "group": "2256",
        "age": 23,
        "marks": [4, 5, 4, 5, 4]
    },
    {
        "name": "Иван",
        "group": "2256",
        "age": 24,
        "marks": [4, 3, 2, 3, 4]
    },
    {
        "name": "Алексей",
        "group": "2255",
        "age": 25,
        "marks": [5, 5, 3, 5, 5]
    },
    {
        "name": "Елизавета",
        "group": "2255",
        "age": 22,
        "marks": [4, 3, 5, 5, 5]
    },
    {
        "name": "Кристина",
        "group": "2255",
        "age": 24,
        "marks": [2, 5, 4, 3, 5]
    }    
]
console.log(groupmates);


var rpad = function(str, length) {
    str = str.toString();
    while (str.length < length)
        str = str + ' ';
    return str;
};

var printStudents = function(students){
    console.log(
        rpad("Имя", 15),
        rpad("Группа", 10),
        rpad("Возраст", 10),
        rpad("Оценки", 20)
    );

    for (var i = 0; i < students.length; i++){
        console.log(
            rpad(students[i].name, 15),
            rpad(students[i].group, 10),
            rpad(students[i].age, 10),
            rpad(students[i].marks, 20)
        );
    }
};

printStudents(groupmates);

// Функция фильтрации по группе
var filterByGroup = function(students, groupName){
    var result = [];

    for (var i = 0; i < students.length; i++){
        if (students[i].group === groupName){
            result.push(students[i]);
        }
    }

    return result;
};

// пример
var filtered = filterByGroup(groupmates, "912-2");
printStudents(filtered);