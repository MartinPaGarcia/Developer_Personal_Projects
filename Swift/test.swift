var fruit = ["apple", "banana", "orange"]  // Array of strings  
print (fruit)


// No information is required to assing an empty array or dictionary to a new variable, or another place
// where there is no information, you need to specify the type

let emptyArray:[String] = []
let emptyDictionary:[String: Float] = [:]

// Control Flow

 
// if and switch to make conditionals, used for loops and while to make loops, Parantheses around the conditions
// or loop variable are optional. Braces around the body are required.


let individualScores = [75, 43, 103, 87, 12]
var teamScore = 0

for score: Int in individualScores{
    if score > 50 {
        teamScore += 3
    }
    else {
        teamScore += 1
    }
    }

print(teamScore)