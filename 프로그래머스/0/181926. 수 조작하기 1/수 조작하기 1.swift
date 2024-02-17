import Foundation

func solution(_ n:Int, _ control:String) -> Int {
    var answer = n
    for i in Array(control) {
        if i == "w" {
            answer += 1
        } else if i == "s" {
            answer -= 1
        } else if i == "d" {
            answer += 10
        } else {
            answer -= 10
        }
    }
    return answer
}