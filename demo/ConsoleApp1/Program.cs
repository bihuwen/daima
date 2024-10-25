using ConsoleApp1;
using ConsoleApp1.Models;

internal class Program
{
    private static void Main(string[] args)
    {
        //没有泛型的情况下
        Class1 noMethod=new Class1();
        Teacher teacher=new Teacher();
        string teaTypeName=noMethod.GetClassType(teacher);
        Console.WriteLine(teaTypeName);
        Student student = new Student();
        string stuTypeName = noMethod.GetClassType(student);
        Console.WriteLine(stuTypeName);
    }
}