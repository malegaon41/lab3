// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    struct Student {
        uint rollNo;
        string name;
        uint marks;
    }

    // Dynamic array to store student details
    Student[] public students;

    // Add a new student
    function addStudent(uint _rollNo, string memory _name, uint _marks) public {
        Student memory newStudent = Student({
            rollNo: _rollNo,
            name: _name,
            marks: _marks
        });
        students.push(newStudent);
    }

    // Get total number of students
    function getTotalStudents() public view returns (uint) {
        return students.length;
    }

    // Fallback and receive functions
    fallback() external payable {}
    receive() external payable {}
}
