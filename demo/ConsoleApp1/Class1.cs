using ConsoleApp1.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public class Class1
    {
        public string GetClassType(Teacher teacher)
        {
        return teacher.GetType().Name;
        }
        public string GetClassType(Student student)
        {
            return student.GetType().Name;
        }
        public string GetClassType(Worker worker)
        {
            return worker.GetType().Name;
        }
        public int GetInt(string str) 
        {
            return int.Parse(str);
        }
        public float GetFL(string str)
        {
            return float.Parse(str);
        }
    }
}
