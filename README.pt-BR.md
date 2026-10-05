<p align="center">
  <img src="assets/banner.svg" alt="Ágora — compreensão profunda e raciocínio aplicado. Uma skill para Claude em qualquer idioma." width="100%">
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.es.md">Español</a> · <b>Português</b>
</p>

<p align="center">
  <b>Um sistema operacional de aprendizagem que transforma o Claude em quem desenha o seu plano,<br>
  conduz as sessões, faz de tutor socrático e avalia o seu progresso, no seu idioma.</b>
</p>

---

## Por que existe

Reler, sublinhar e acumular horas *parece* produtivo, mas rende pouco. As técnicas que mais funcionam (lembrar sem olhar, espaçar as revisões, tentar antes de ver a solução, explicar e receber crítica) são desconfortáveis e difíceis de manter sem alguém que guie.

A Ágora é esse alguém. Ela pega as práticas mais transferíveis das universidades de referência e as transforma num ciclo diário, mensurável e adaptativo, que funciona para qualquer matéria e em qualquer idioma.

> **A Ágora não promete aumentar o QI e nunca o mede.** Ela treina e mede **desempenho observável**: compreensão profunda, transferência para problemas novos, clareza ao explicar e qualidade do que você produz.

## O que faz

| Modo | O que acontece |
|---|---|
| **Início** | 6 perguntas (objetivo, matéria, perfil, tempo, energia, com quem você discute) e a criação do seu caderno de progresso. |
| **Diagnóstico** | 85 minutos (ou em 2 partes, ou em 3 dias de 30): leitura, memória, lógica, problemas, escrita, explicação, metacognição e atenção. Define o nível: Fundamentos, Intermediário, Avançado ou Intensivo. |
| **Plano de 12 semanas** | Cada semana treina uma habilidade cognitiva usando o conteúdo da *sua* matéria. |
| **Sessão diária** | Rotinas exatas de 30, 60, 120 ou 180 minutos em 7 passos. |
| **Tutoria socrática** | Não entrega a resposta: pede a sua tentativa, questiona suposições, traz contraexemplos e aumenta a dificuldade, com uma escada de dicas de H1 a H5. |
| **Modo atenção** | Formato opcional pensado para o TDAH: blocos de 10 a 20 minutos com uma única tarefa visível, pausas com movimento, ritual de início, no máximo 8 cartões por dia, retornos em vez de sequências e um freio para o hiperfoco. |
| **Seu material** | Lê seus PDFs, anotações e ementa, conecta tudo ao plano e cria cartões e problemas que citam as páginas. Provas antigas ficam reservadas para o teste final. |
| **Revisão espaçada** | Agendamento com FSRS-6 por um script sem dependências (sem Python, usa caixas de Leitner). |
| **Revisões** | Métricas semanais e mensais, com regras explícitas para subir ou baixar a dificuldade. |
| **Projetos** | Projetos finais de STEM, humanidades, negócios/decisão, design e idiomas. |
| **Manual** | Gera o sistema completo como documento, no seu idioma. |

Serve para estudantes do ensino médio avançado, universitários, profissionais aprendendo uma habilidade complexa e autodidatas sem professor.

## Qualquer idioma

A skill está escrita em inglês e **fala com cada pessoa no idioma dela** (português, espanhol, italiano, francês, alemão, inglês…): perguntas, feedback, rubricas, modelos e o prompt do tutor. Os nomes de arquivo continuam em inglês para que os scripts funcionem.

Quando a matéria *é* um idioma, as instruções chegam no seu idioma e a prática acontece no idioma-alvo, com mais imersão conforme o nível sobe (cerca de 30 % → 60 % → 90 %). Veja [uma sessão de exemplo aprendendo inglês](examples/session-30-min.pt-BR.md).

## Modo atenção (pensado para o TDAH)

É opcional e nunca faz diagnóstico. Mantém os métodos que também funcionam com TDAH (a prática de lembrança ajuda tanto quanto aos colegas) e muda o formato: blocos curtos com uma única tarefa visível, pausas com movimento, planos "se… então…" para as distrações, uma lista de pendências, uma microssessão de 10 minutos para dias de pouca energia, revisões limitadas, retornos em vez de sequências e avisos de tempo para que o hiperfoco não roube horas de sono. Não dá conselhos sobre medicação nem oferece "treino cerebral", que não melhora os sintomas nem as notas em avaliações cegas. Veja [`agora/references/attention.md`](agora/references/attention.md).

## Instalação

**Um comando (qualquer agente compatível com skills).**

```bash
npx skills add Mlle-LondonG/agora-skill
```

**Plugin do Claude Code.** Dentro de uma sessão:

```text
/plugin marketplace add Mlle-LondonG/agora-skill
/plugin install agora@agora-skill
```

**App do Claude (web ou desktop).** Baixe o [`agora.zip`](agora.zip) (ou o anexado à [versão mais recente](../../releases/latest)) e envie na seção de Skills das configurações.

**Claude Code, manualmente.** Copie a pasta `agora/` para as suas skills pessoais ou para as de um projeto:

```bash
git clone https://github.com/Mlle-LondonG/agora-skill.git
cp -r agora-skill/agora ~/.claude/skills/          # para todos os seus projetos
# ou: cp -r agora-skill/agora .claude/skills/      # só para este projeto
```

**Outra IA.** `agora/references/tutor.md` traz um prompt de tutor socrático pronto para colar (peça à Ágora e ele vem traduzido).

## Como começar

Escreva **"Ágora"** numa conversa. Na primeira vez, ela faz as perguntas iniciais e propõe o diagnóstico. Depois:

```text
Ágora, sessão de 60 minutos
Ágora, tutoria sobre recursão
Ágora, como estou indo?
Ágora, travei nas integrais
Ágora, aqui estão minhas anotações (anexe os PDFs)
Ágora, me dá o manual completo
```

## O método

### Cada sessão

| Passo | 30 min | 60 min | 120 min | 180 min |
|---|---|---|---|---|
| 1. Definir o resultado | 1 | 2 | 3 | 5 |
| 2. Lembrar sem olhar | 5 | 10 | 15 | 20 |
| 3. Estudar com uma pergunta-guia | 7 | 15 | 30 | 45 |
| Pausa | — | — | 5 | 10 |
| 4. Resolver algo difícil | 9 | 18 | 35 | 50 |
| Pausa | — | — | — | 5 |
| 5. Explicar e defender | 4 | 7 | 15 | 20 |
| 6. Corrigir com evidências | 2 | 5 | 10 | 15 |
| 7. Registrar e espaçar | 2 | 3 | 7 | 10 |

### As 12 semanas

| Fase | Semanas | Competências |
|---|---|---|
| **I. Base do sistema** | 1–4 | Atenção profunda · memória e calibração · primeiros princípios · leitura crítica |
| **II. Raciocínio** | 5–8 | Lógica e causalidade · probabilidade e decisão · problemas quantitativos · escrita e defesa oral |
| **III. Transferência e produção** | 9–12 | Criatividade e hipóteses · transferência · projeto integrador · defesa e diagnóstico final |

### Dificuldade adaptativa

| Se a lembrança sem anotações for… | A Ágora… |
|---|---|
| menor que 60 % | não traz conteúdo novo: lembrança, exemplos resolvidos e pré-requisitos |
| 60–79 % | reduz o conteúdo novo pela metade e dobra a prática de lembrança |
| 80–90 % | mantém a dificuldade e espaça as revisões |
| maior que 90 % duas vezes **e** com transferência | aumenta a complexidade |

Diante de falhas repetidas, distingue cinco causas, nesta ordem: cansaço, pré-requisitos, estratégia, falta de feedback ou dificuldade excessiva. Inclui regras de descanso (6+1, teto diário, sono) para evitar o esgotamento.

### O que vem de cada instituição

| | Prática | Na Ágora |
|---|---|---|
| **Harvard** | Método do caso, instrução por pares | Caso semanal com decisão defendida; colegas simulados |
| **MIT** | Aprender fazendo, listas de problemas rigorosas | A maior parte de cada sessão é resolvendo |
| **Cambridge** | Supervisões em grupos muito pequenos | Produção semanal defendida diante do tutor |
| **Stanford** | Design, prototipagem e iteração | Semana de criatividade e projeto de design |

Nenhuma dessas universidades usa um único método; a Ágora adota práticas concretas, não "o método X".

## Seu caderno

Com acesso a uma pasta, a Ágora guarda seu progresso em arquivos; sem isso, entrega um bloco de estado para você colar na próxima vez. Comece pelo [`notebook-template/`](notebook-template): `profile.md` (objetivo, nível, plano), `sessions.csv` (uma linha por sessão), `errors.md` (erros por tipo), `cards.csv` (cartões com estado FSRS e páginas da fonte), `reviews.md` (revisões) e `sources.md` (seu material).

```bash
python3 agora/scripts/fsrs.py due cards.csv              # o que revisar hoje
python3 agora/scripts/fsrs.py review cards.csv c12 good  # registrar uma revisão
python3 agora/scripts/metrics.py sessions.csv --days 7   # resumo semanal + regra sugerida
```

O `fsrs.py` adapta o FSRS-6 do [py-fsrs](https://github.com/open-spaced-repetition/py-fsrs); em 1.924 revisões simuladas, as datas coincidiram exatamente com as da biblioteca de referência.

## Evidências e limites

Cada prática é marcada como **evidência sólida**, **evidência moderada** ou **sugestão prática**. As referências estão em [`agora/references/evidence.md`](agora/references/evidence.md).

A Ágora **não substitui ajuda profissional** para TDAH, ansiedade, depressão, distúrbios do sono ou outras condições.

## Contribuir

Usou e algo não funcionou, ou tem uma ideia? Abra uma *issue* contando o que aconteceu, o que você esperava e, se puder, um trecho da conversa.

## Licença

[MIT](LICENSE) · Feito por [@Mlle-LondonG](https://github.com/Mlle-LondonG).
