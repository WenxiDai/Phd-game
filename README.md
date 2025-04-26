# PhD Simulator

A text-based game simulating the life of a PhD student with random events, challenges, and decisions that reflect the real-life struggles and triumphs of pursuing a doctoral degree.

## How to Run

To run this game, run the code in the terminal section as follows:

```
npm run build && npm start
```

This will create a local server. Then open your browser and go to:

```
http://localhost:8000/new
```

## About the Game

PhD Simulator is a text-based random event-driven game that models the typical experiences of a PhD student. You'll face various challenges such as:

- Managing your time between reading papers and conducting experiments
- Dealing with broken lab equipment
- Writing and submitting papers to academic journals
- Handling rejection and revision of papers
- Preparing for qualifying exams
- Navigating the ups and downs of advisor relationships
- Balancing work and mental health

Your goal is to publish the required number of papers to qualify for your degree before running out of hope or time!

## Game Mechanics

- **Hope Meter**: Your mental wellbeing that goes up and down as events unfold
- **Time Meter**: Tracks your progress through the years of your PhD
- **Items**: Collect ideas, develop preliminary results, create major results, and generate figures to write papers
- **Status Effects**: Various conditions that affect your gameplay (exhaustion, upgraded equipment, etc.)

## Key Features

- Random event system makes each playthrough unique
- Resource management between papers, results, and experiments
- Strategic decisions between short-term gains and long-term success
- Multiple paths to victory and failure
- Realistic representation of academia with a touch of humor

## Customization

The game uses YAML files for event definitions, making it highly modifiable. You can find these files in the `static/rulesets/default` directory.

## Credits

Original game developed by Mianzhi Wang, modified and enhanced for this version.

## License

MIT License