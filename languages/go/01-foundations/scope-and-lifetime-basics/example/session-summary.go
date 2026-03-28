// This extra example extends scope and lifetime basics with a session summary.
// Example purpose: keep temporary variables local to helper functions.

package main

import "fmt"

const bonusPoints = 5
const passingScore = 70

func summarizeAttempt(name string, score int) (string, bool) {
	effectiveScore := score + bonusPoints
	passed := effectiveScore >= passingScore
	status := "needs review"
	if passed {
		status = "passed"
	}

	return fmt.Sprintf("%s: raw=%d, effective=%d, status=%s", name, score, effectiveScore, status), passed
}

func main() {
	attempts := []struct {
		name  string
		score int
	}{
		{"Ana", 64},
		{"Bruno", 71},
		{"Carla", 58},
	}

	passedCount := 0
	for _, attempt := range attempts {
		line, passed := summarizeAttempt(attempt.name, attempt.score)
		fmt.Println(line)
		if passed {
			passedCount++
		}
	}

	fmt.Printf("Students above the target: %d\n", passedCount)
}
