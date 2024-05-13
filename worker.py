from meloetta.workers import SelfPlayWorker
from meloetta.actors.base import Actor, Ran

def run_workers():
    worker = SelfPlayWorker(
        worker_index=0,
        num_players=2,  # 2 is players per worker
        battle_format="gen9randombattle",
        team="null",
        actor_fn=choose_action,
        actor_args=(), # Optional args to be called when instantiating your actor
        actor_kwargs={}, # Optional kwargs to be called when instantiating your actor
    )
    worker.run()


def choose_action(
    self,
    state: State,
    room: BattleRoom,
    choices: Choices,
):
    random_key = random.choice([key for key, value in choices.items() if value])
    _, (func, args, kwargs) = random.choice(list(choices[random_key].items()))
    return func, args, kwargs


if __name__ == "__main__":
    run_workers()