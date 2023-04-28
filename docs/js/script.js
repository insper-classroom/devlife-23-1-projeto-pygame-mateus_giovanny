//essa função eu peguei no chatGPT, mas mudei algumas coisas :)
// Função para buscar o histórico de commits do Git e gerar a tabela
function gerarLogDeDesenvolvimento() {
    fetch('https://api.github.com/repos/insper-classroom/devlife-23-1-projeto-pygame-mateus_giovanny/commits')
    .then(response => response.json())
    .then(commits => {
        const tbody = document.querySelector('#log-table tbody');

        for (const commit of commits) {
        const tr = document.createElement('tr');
        const autorTd = document.createElement('td');
        const dataTd = document.createElement('td');
        const mensagemTd = document.createElement('td');

        autorTd.textContent = commit.commit.author.name;
        dataTd.textContent = formatDate(commit.commit.author.date, 'dd/mm/aaaa');
        mensagemTd.textContent = commit.commit.message;

        tr.appendChild(autorTd);
        tr.appendChild(dataTd);
        tr.appendChild(mensagemTd);

        tbody.appendChild(tr);
        }
    });
}

function formatDate(string, format) {
    const map = {
        dd: string.slice(8,10),
        mm: string.slice(5,7),
        aaaa: string.slice(0,4)
    }

    return format.replace(/dd|mm|aaaa/gi, matched => map[matched])
}

function scrollToContent(id) {
    const contentSection = document.getElementById(id);
    var menu = document.querySelector('header')
    window.scrollTo({
      top: contentSection.offsetTop - menu.offsetHeight,
      behavior: 'smooth'
    });
}
// Chama a função para gerar a tabela quando a página é carregada
gerarLogDeDesenvolvimento();