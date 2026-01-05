from langchain_openai import ChatOpenAI

from classmate.backend.infrastructure.environs import Environs
from classmate.backend.prompts.prompt import Prompt

environs = Environs()

transcription_example = """
Cláudia: ...Certo, Roberto. Eu entendi que o produto tem uma aceitação técnica muito boa. O feedback de quem usa é positivo. Mas voltando aos números que você me mostrou na tela anterior: por que a receita estagnou nos últimos três meses se o mercado está aquecido?

Roberto: Então, é isso que está tirando meu sono. A gente fecha vendas, sabe? Mas parece que o esforço para trazer um cliente novo dobrou. Hoje, 80% da minha base vem de indicação. O "boca a boca" funciona, mas eu não tenho controle sobre ele.

Cláudia: Exato. Indicação é ótimo para validação, mas péssimo para previsibilidade. Você não consegue "aumentar o volume" da indicação quando quer crescer. Como está estruturado o seu time de vendas hoje? Quem faz a prospecção ativa?

Roberto: Basicamente, sou eu e mais um vendedor júnior. A gente pega umas listas, manda e-mail frio e tenta agendar demonstração. Mas a taxa de resposta é ridícula. E quando agendamos, muitas vezes o cara não tem budget.

Cláudia: Entendi. O problema aqui parece ser qualificação, não fechamento. Vocês estão gastando energia de sócio – a sua energia, que é cara – falando com leads frios que nem perfil de compra têm. Vocês têm um ICP (Perfil de Cliente Ideal) definido ou estão atirando para todo lado?

Roberto: A gente tem uma ideia... Pequenas e médias indústrias. Mas, na prática, se aparecer uma loja de varejo querendo comprar, a gente vende.

Cláudia: Aí está o primeiro gargalo. Quem vende para todo mundo, não fala a língua de ninguém. Se a gente não nichar esse discurso, o CAC (Custo de Aquisição de Cliente) vai continuar subindo. Vamos precisar separar as funções: colocar alguém focado só em pré-vendas (SDR) para limpar esses leads antes de chegarem em você. E sobre o modelo de cobrança, é mensalidade recorrente ou pagamento único?

Roberto: É recorrente (SaaS). Mas o churn [cancelamento] aumentou um pouco também. O cliente entra, usa três meses e para.

Cláudia: Se ele para em três meses, o erro está na venda ou no onboarding. Provavelmente vendemos a expectativa errada ou ele não viu valor rápido o suficiente. Vamos fazer o seguinte: para a próxima sessão, eu preciso que você me traga a gravação de duas reuniões de vendas recentes e o mapa do processo de implementação do cliente. Eu suspeito que estamos colocando gente para dentro que não deveria estar lá, só para bater meta de curto prazo.

Roberto: Faz sentido. Às vezes a gente força a venda para fechar o caixa do mês e depois o operacional sofre.

Cláudia: Exatamente. Venda ruim vira churn rápido. Vamos focar em estruturar essa máquina de aquisição para ela rodar sem depender 100% do seu networking.
"""

class ChainSummary:
    def __init__(self):
        self._chat = ChatOpenAI()
        self._prompt = Prompt()

    def generate_summary(self, transcription: str):
        prompt = self._prompt.prompt_summary_transcription.format(transcription=transcription)
        res = self._chat.invoke(prompt)
        return res.content

if __name__ == "__main__":
    chain_summary = ChainSummary()
    res = chain_summary.generate_summary(transcription_example)
    print(res)
    pass