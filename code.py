  def minimax_plain(b: List[str], depth: int, is_max: bool, 
                    ai: str, human: str) -> Tuple[int, Optional[int], int]:
      # Count this node as explored
      nodes = 1
      # Check if current position is a terminal state (win/loss/draw)
      term = evaluate_terminal(b, ai, depth)
      if term is not None:
          # Return evaluation score, no move, and node count for leaf nodes
          return term, None, nodes
  
      best_move = None  # Track the best move found at this node
  
      if is_max:  # AI's turn (Maximizer) - trying to get highest score
          best_val = -10_000  # Initialize to very low value
          # Try every legal move the AI can play
          for mv in legal_moves(b):
              # Simulate AI playing at this position
              child = apply_move(b, mv, ai)
              # Recursively evaluate opponent's response (minimizer's turn)
              val, _, c_nodes = minimax_plain(child, depth+1, False, ai, human)
              nodes += c_nodes  # Accumulate total nodes explored
  
              # Keep track of the move with highest score
              if val > best_val:
                  best_val = val
                  best_move = mv
          # Return the best score achievable and the move that gets it
          return best_val, best_move, nodes
      else:  # Human's turn (Minimizer) - trying to get lowest score for AI
          best_val = 10_000  # Initialize to very high value
          # Try every legal move the human can play
          for mv in legal_moves(b):
              # Simulate human playing at this position
              child = apply_move(b, mv, human)
              # Recursively evaluate AI's response (maximizer's turn)
              val, _, c_nodes = minimax_plain(child, depth+1, True, ai, human)
              nodes += c_nodes  # Accumulate total nodes explored
  
              # Keep track of the move with lowest score (worst for AI)
              if val < best_val:
                  best_val = val
                  best_move = mv
          # Return worst-case score from AI's perspective
          return best_val, best_move, nodes
