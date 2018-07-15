" Status Line {{{
" 
function! Relpath()
    if &ft == "help" || &ft == "man.cpp"
        return expand("%:t")
    endif

    let file_drive = expand("%:p")[0]
    let dir_drive = getcwd()[0]

    if file_drive != dir_drive
        return expand("%") 
    endif

    let filename = expand("%:p")
    let cwd = getcwd()

    let index = 0
    let length = len(cwd)

    while index < length
        if filename[index] != cwd[index]
            break
        endif
        let index = index + 1
    endwhile

    let file_not_in_cd = index < length
    if file_not_in_cd
        let dir_count = count(cwd[index:], '\') + 1
        let ret_val = repeat('..\', dir_count) . filename[index-1:]
        let ret_val = substitute(ret_val, '\\\\', '\\', 'g')
        return ret_val
    else
        return expand("%")
    endif

endfunction
set statusline=%<%{Relpath()}
set statusline+=%m%r%y%w%=%l/%-6L\ %3c 
" set statusline=%f%m%r%y%w%=%l/%-6L\ %3c 
" }}}
" Error Lines {{{
let g:last_command = ""
let g:error_buffers = []
let g:error_lines = []
let g:messages = []
sign define piet text=>> texthl=MatchParen linehl=Normal
function! ParseQuickfix()
    let last_cmd = histget("cmd", histnr("cmd"))
    if last_cmd[:4] != "make"
        return
    endif
    sign unplace *
    let g:error_lines = []
    let g:messages = []
    let index = 0
    let Q = getqflist()
    let len = len(Q)
    while index < len
        call add(g:error_lines, Q[index]["lnum"])
        call add(g:messages, Q[index]["text"])
        call add(g:error_buffers, Q[index]["bufnr"])
        exe ":sign place 2 line=" . Q[index]["lnum"] . " name=piet buffer=". Q[index]["bufnr"]
        let index = index + 1
    endwhile
    if len == 0
        cclose
        redraw | echohl ModeMsg | echo "Build succeeded" | echohl Normal
    else
        copen
    endif
endfunction

function! PrintErrorMsg()
    let lnum = line(".")
    let bufnum = bufnr("%")
    let len = len(g:error_lines)
    let index = 0
    let on_error_line = v:false
    let echo_message = ""
    while index < len
        if g:error_lines[index] == lnum && g:error_buffers[index] == bufnum
            let echo_message =  g:messages[index]
        endif
        let index = index + 1
    endwhile
    if echo_message != ""
        redraw | echohl ErrorMsg | echo  echo_message | echohl Normal
    endif
endfunction

au! CursorMoved *
au! QuickFixCmdPost *
au CursorMoved * call PrintErrorMsg()
au QuickFixCmdPost * call ParseQuickfix()
" }}}
" Traverse Indent {{{
function! AddPositionToJumpList()
    let save_a_mark = getpos("'a")
    normal! ma
    normal! `a
    call setpos("'a", save_a_mark)
endfunction

function! PreviousIndent()
    call AddPositionToJumpList()
    let previous_indent = indent(".") - 1
    if previous_indent == -1
        let previous_indent = 0
    endif
    let regexp = printf('^\s\{0,%d\}\S', previous_indent)
    call search(regexp, 'be')
endfunction

nnoremap <silent> <BS> :call PreviousIndent()<CR>
" }}}

