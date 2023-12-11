use std::fs;
// use std::env;
use std::collections::HashMap;
fn
main(){
    // Open the file in read-only mode
    // let filename = String::from("ex.in");
    let filename = String::from("p8.in");
    println!("In file {}", "main.rs");

    let contents = fs::read_to_string(filename)
      .expect("Should have been able to read the file");
      // let contents = fs::read_to_string("main.rs")
    let lines: Vec<&str> = contents.lines().collect();
   let mut _first_line: String = "LR".to_string();
   let mut _my_map: HashMap<String, (String, String)> = HashMap::new();
    for (index, line) in lines.iter().enumerate() {
       if index <2 {
          if index == 0 {
             _first_line = line.to_string();
          }
          continue;
       }
       let parts: Vec<&str> = line.split(" = ").collect();
       let key = parts[0];
       let ways: Vec<&str> = parts[1][1..parts[1].len()-1].split(", ").collect();


       _my_map.insert(String::from(key), (String::from(ways[0]), String::from(ways[1])));
       println!("{}: {}, {}", key, ways[0], ways[1]);

    }
      let mut c= 0;
      let choice = 0;
      let mut current = String::from("AAA");
      let mut tu: (String, String);
      // let mut left : String;
      // let mut right : String;
      loop{
         if current == "ZZZ"{
            break;
         }
         let mut direction: char;
         let index = c%_first_line.len();
         direction = _first_line.as_bytes()[index] as char;
         let result = _my_map.get(&current);
         if let Some((left, right))  = result{

            match direction{
               'L' => current = left.to_string(),
               'R' => current = right.to_string(),
               _ => todo!(),

            }
         }
         c+=1


       }

         println!("{}: {}", c, current);


}
