function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)  
% X is m*(n+1) matrix   
% y is m*1  
% theta is (n+1)*1 matrix  
% alpha is a number   
% num_iters is number of iterators  
  
      
    m = length(y); % number of training examples  
    J_history = zeros(num_iters, 1);  %cost function的值的变化过程  
    %预先定义了迭代的次数  
  
    for iter = 1:num_iters  
  
        temp1 = theta(1) - (alpha / m) * sum((X * theta - y).* X(:,1));  
        temp2 = theta(2) - (alpha / m) * sum((X * theta - y).* X(:,2));  
        theta(1) = temp1;  
        theta(2) = temp2;  
        J_history(iter) = computeCost(X, y, theta);  
  
    end  
  
end  