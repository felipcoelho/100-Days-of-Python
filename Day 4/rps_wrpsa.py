import random
import matplotlib.pyplot as plt
import networkx as nx

# Official WRPSA rules
RULES = {
    'rock':     {'beats': 'scissors', 'loses': 'paper'},
    'paper':    {'beats': 'rock',     'loses': 'scissors'},
    'scissors': {'beats': 'paper',    'loses': 'rock'}
}

MOVES = list(RULES.keys())

def decide_winner(player, computer):
    if player == computer:
        return 'tie'
    elif RULES[player]['beats'] == computer:
        return 'win'
    else:
        return 'lose'

def play_round():
    player = input(f"Choose your move ({', '.join(MOVES)}): ").strip().lower()
    if player not in MOVES:
        print("Invalid move. Try again.")
        return play_round()
    computer = random.choice(MOVES)
    print(f"Computer chose: {computer}")
    result = decide_winner(player, computer)
    if result == 'tie':
        print("It's a tie! Play again.")
        return play_round()
    elif result == 'win':
        print(f"You win! {player.capitalize()} beats {computer}.")
    else:
        print(f"You lose! {computer.capitalize()} beats {player}.")

def draw_rps_graph():
    G = nx.DiGraph()
    for move, rel in RULES.items():
        G.add_edge(move, rel['beats'], label='beats')
        G.add_edge(move, rel['loses'], label='loses')
    pos = nx.circular_layout(G)
    plt.figure(figsize=(6,6))
    nx.draw(G, pos, with_labels=True, node_color=['#f4a261','#2a9d8f','#e76f51'], node_size=2000, font_size=16, arrowsize=30)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=12)
    plt.title('Rock Paper Scissors Relationships (WRPSA Rules)')
    plt.show()

if __name__ == "__main__":
    draw_rps_graph()
    play_round()
