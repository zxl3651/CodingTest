import Foundation

func solution(_ cipher:String, _ code:Int) -> String {
    var answer = ""
    var arr = cipher.map{ String($0) }
    for i in 0..<arr.count {
        if (i+1) % code == 0 {
            answer += arr[i]
        }
    }
    return answer
}