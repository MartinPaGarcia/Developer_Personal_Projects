// Arrays
func fruits() {
    let fruit:[String] = ["apple", "banana", "orange"]  // Array of strings
    print(fruit)
}

// Empty Arrays and Dictionaries
func emptyArrays() {
    // No information is required to assign an empty array or dictionary to a new variable, or another place
    // where there is no information, you need to specify the type
    // let emptyArray: [String] = []
    // let emptyDictionary: [String: Float] = [:]
}

// Control Flow
func controlFlow() {
    // Use if and switch to make conditionals, use for-in, while, and repeat-while to make loops. Parentheses
    // around the condition or loop variable are optional. Braces around the body are required.
    let individualScores:[Int] = [75, 43, 103, 87, 12]
    var teamScore = 0
    for score in individualScores {
        if score > 50 {
            teamScore += 3
        } else {
            teamScore += 1
        }
    }
    print(teamScore)

    let scoreDecoration:String = if teamScore > 10 {
        "You win!"
    } else {
        "You lose!"
    }
    print("Score: ", teamScore, "", scoreDecoration)
}

func main() {
    fruits()
    controlFlow()
}

main()
